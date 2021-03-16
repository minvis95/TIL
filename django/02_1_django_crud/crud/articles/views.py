from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # 모든 게시글을 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)

# articles = Article.objects.all()[::-1]
# articles = Article.objects.order_by('-pk')