# user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),  # 更新为 login_view
    path('register/', views.register, name='register'),
]