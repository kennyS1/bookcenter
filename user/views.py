# user/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # 使用别名避免冲突
from django.contrib import messages
from user.models import User

def index(request):
    return render(request, "userIndex.html")

def login_view(request):
    if request.method == "POST":
        # 接收表单数据
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 验证数据
        if not all([username, password]):
            messages.error(request, "字段不能为空！")
            return render(request, "login.html")

        # 验证用户身份
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # 用户验证成功，登录
            auth_login(request, user)
            messages.success(request, "登录成功！")
            return redirect("index")
        else:
            # 用户验证失败
            messages.error(request, "用户名或密码错误！")
            return render(request, "login.html")

    # GET 请求，显示登录页面
    return render(request, "login.html")



def register(request):
    if request.method == "POST":
        # 接收表单数据
        username = request.POST.get("username")
        password = request.POST.get("password1")
        confirm_password = request.POST.get("password2")

        # 验证数据
        if not all([username, password, confirm_password]):
            messages.error(request, "所有字段都是必填的！")
            return render(request, "register.html")

        if password != confirm_password:
            messages.error(request, "两次输入的密码不一致！")
            return render(request, "register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "用户名已存在！")
            return render(request, "register.html")

        # 创建用户
        try:
            user = User.objects.create_user(
                username=username,
                password=password,
            )
            user.save()
            login(request, user)  # 现在调用的是 django.contrib.auth.login
            messages.success(request, "注册成功！")
            return redirect("register")
        except Exception as e:
            messages.error(request, f"注册失败：{str(e)}")
            return render(request, "register.html")

    return render(request, "register.html")