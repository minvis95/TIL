import random
from django.shortcuts import render

# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    # templates 경로안에 있어야한다. T는
    return render(request, 'articles/index.html')    # render 함수의 첫번째 인자는 request

def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Harry'
    }
    context = {
        'info': info,
        'foods': foods,
    }

    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['족발', '피자', '햄버거', '초밥',]
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # request에서 get에 위치해 있어. 위치해있는 값은 dict이여서 key인 message로 접근
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/hello.html', context)

def detail(request, article_num):
    context = {
        'article_num': article_num
    }
    return render(request, 'articles/detail.html', context)

def dtl_practice(request):
    students = ['민찬우', '민준우', '이현지', '이상민']
    fruits = ['사과', '바나나', '포도', '감', '수박']
    user_list = []
    context = {
        'students': students,
        'fruits': fruits,
        'user_list': user_list,
    }

    return render(request, 'articles/dtl_practice.html', context)