import random
from django.shortcuts import render

# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    # templates 경로안에 있어야한다. T는
    return render(request, 'index.html')    # render 함수의 첫번째 인자는 request

def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Harry'
    }
    context = {
        'info': info,
        'foods': foods,
    }

    return render(request, 'greeting.html', context)

def dinner(request):
    foods = ['족발', '피자', '햄버거', '초밥',]
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'dinner.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # request에서 get에 위치해 있어. 위치해있는 값은 dict이여서 key인 message로 접근
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)

def detail(request, article_num):
    context = {
        'article_num': article_num
    }
    return render(request, 'detail.html', context)