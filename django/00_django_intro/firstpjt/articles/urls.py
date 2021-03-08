from django.urls import path
# 명시적 상대경로 표현
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
    # 주소자체를 변수로 설정하여 동적으로 작동
    # path('hello/<name>/', views.hello),
    # 'articles/1/'로 요청했을 경우 뷰 함수의 detail 수행
    path('<int:article_num>', views.detail, name='article_num'),
]