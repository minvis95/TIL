from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.http import HttpResponse, HttpResponseForbidden
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
import hashlib

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
        # return HttpResponseForbidden()
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
        

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('articles:detail', article.pk)
        context = {
            'comment_form': comment_form,
            'article': article,
        }
        return render(request, 'articles/detail.html', context)
    return redirect('accounts:login')
    # return HttpResponse(status=401)


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        # return HttpResponseForbidden()
    return redirect('articles:detail', article_pk)
    # return HttpResponse(status=401)

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
        # if request.user in article.like_users.all():
            # 좋아요 취소
            article.like_users.remove(request.user)
        else:
            # 좋아요 누름
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')

"""
# [참고] 쿼리셋 효과적으로 사용하기
# https://docs.djangoproject.com/en/3.1/topics/db/queries/#querysets-are-lazy
# https://docs.djangoproject.com/en/3.1/ref/models/querysets/#when-querysets-are-evaluated
# https://docs.djangoproject.com/en/3.1/topics/db/queries/#caching-and-querysets

# 실제 쿼리셋을 만드는 작업에는 DB 작업이 포함되지 않음 
q = Entry.objects.filter(title__startswith="What")
q = q.filter(created_at__lte=datetime.date.today())
q = q.exclude(context__icontains="food")
print(q) # 여기서 평가 됨


# Iteration
# 쿼리셋은 반복 가능하며 처음 반복할 때 데이터베이스 쿼리를 실행(평가)
for e in Entry.objects.all():
    pass

# bool()
if Entry.objects.filter(title__'test'):
    pass


# 나쁜 예
print([e.headline for e in Entry.objects.all()]) # 평가
print([e.pub_date for e in Entry.objects.all()]) # 평가

# 좋은 예
queryset = Entry.objects.all()
print([p.headline for p in queryset]) # Evaluate the query set. (평가)
print([p.pub_date for p in queryset]) # Re-use the cache from the evaluation. (캐시에서 재사용)


# 캐시 되지않는 경우
queryset = Entry.objects.all()
print(queryset[5]) # Queries the database
print(queryset[5]) # Queries the database again

# 위 상황을 방지하고 싶을 때
queryset = Entry.objects.all()
[entry for entry in queryset] # Queries the database (전체 쿼리셋을 평가 시켜버림)
print(queryset[5]) # Uses cache
print(queryset[5]) # Uses cache



# 우리의 LIKE 코드를 예시로 사용해보자
like_set = article.like_users.filter(pk=request.user.pk)
if like_set: # 평가
    # 쿼리셋의 전체 결과가 필요하지 않은 상왕임에도
    # ORM은 전체 결과를 가져옴
    article.like_users.remove(request.user) 

# 개선 1
# exists() 쿼리셋 캐시를 만들지 않으면서 특정 레코드가 있는지 검사
if like_set.exists():
    # DB에서 가져온 레코드가 없다면
    # 메모리를 절약할 수 있다
    article.like_users.remove(request.user)


# 만약 IF 문안에서 반복문이 있다면?

# if에서 평가 후 캐싱
if like_set:
    # 순회할때는 위에서 캐싱된 쿼리셋을 사용
    for user in like_set:
        print(user.username)


# 만약 쿼리셋 자체가 너무너무 크다면??
# interator()
# 데이터를 작은 덩어리로 쪼개서 가져오고, 이미 사용한 레코드는 메모리에서 지움
# 전체 레코드의 일부씩만 DB에서 가져오므로 메모리를 절약
if like_set:
    for user in like_set.iterator():

# 그런데 쿼리셋이 너무너무 크다면 if 평가에서도 버거움
if like_set.exists():
    for user in like_set.iterator():
        pass
"""
