import random
import time

from django.contrib import auth
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from uauth.models import User, RequestCount


def regist(request):
    if request.method == "GET":
        return render(request,'day6_register.html')
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        password = make_password(password) # 对password进行加密

        User.objects.create(
            u_name=name,
            u_password=password
        )
        return HttpResponseRedirect('/uauth/login/')

def login(request):
    if request.method == "GET":
        return  render(request,'day6_login.html')
    if request.method == "POST":
        # 如果登录成功，绑定参数到cookie中，set_cookie()
        name = request.POST.get("name")
        password = request.POST.get("password")

        if User.objects.filter(u_name=name).exists(): # 如果用户名存在
            user = User.objects.get(u_name=name)
            if check_password(password,user.u_password): # 验证密码
                # ticket = 'lalala'
                s = 'abcdefghijklmnopqrstuvwxyz1234567890'
                ticket = ""
                for i in range(15):
                    # 获取随机的字符串，每次获取一个字符
                    ticket += random.choice(s)
                now_time = int(time.time()) # time.time():1970.1.1到现在的秒数 int: 截去小数部分
                ticket = 'TK_' + ticket + str(now_time)
                # 绑定令牌到cookie里面
                # response = HttpResponse("登录成功")  # 实例化一个响应
                response = HttpResponseRedirect("/stuapp/index")
                response.set_cookie('ticket',ticket,max_age=1000) # max_age=1000：在浏览器最大存活时间为1000秒
                # 存在数据库中
                user.u_ticket = ticket
                user.save()
                return response
            else:
                # return HttpResponse("用户密码错误！！")
                return render(request, "day6_login.html", {'password': '用户密码错误'})
        else:
            # return HttpResponse("用户不存在！！")
            return render(request,"day6_login.html",{'name':'用户不存在'})

def logout(request):
    if request.method == "GET":
        response = HttpResponseRedirect('/uauth/login/')
        response.delete_cookie('ticket')
        return response

def requestCount(request):
    if request.method == "GET":
        requestcount = RequestCount.objects.all()
        return render(request, "requestCount.html", {'requestcount': requestcount})

def djLogin(request):
    if request.method == "GET":
        return render(request,"login.html")
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        # 验证用户名和密码，通过的话，返回user对象
        user = auth.authenticate(username=name,password=password)
        if user: # 验证成功
            auth.login(request,user)
            return HttpResponseRedirect("/stuapp/index/")
        else:
            return render(request,"index.html")

from django.contrib.auth import models
def djRegist(request):
    if request.method == "GET":
        return render(request,'day6_register.html')
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        models.User.objects.create_user(
            username=name,
            password=password
        )
        return HttpResponseRedirect('/uauth/djlogin/')

def djLogout(request):
    if request.method == "GET":
        auth.logout(request)
        return HttpResponseRedirect('/uauth/djlogin/')