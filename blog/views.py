import random
import time
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import User, Article, Type
from .cookie import checkcookie
from django.core.paginator import Paginator

def index(request):
    context = {}
    if request.method == 'GET':
        context['分类'] = Type.objects.all()
        if checkcookie(request, User) is True:
            context['判断'] = True
            cookie = request.COOKIES.get('cookie')
            context['user'] = User.objects.get(cookie=cookie).username
            return render(request, 'blog/index.html', context)
        else:
            return render(request,'blog/index.html',context)

def regist(request):
    context = {}
    context['分类'] = Type.objects.all()
    if request.method == 'POST':
        username = request.POST['用户名']
        password = request.POST['密码']
        password1 = request.POST['确认密码']
        if User.objects.filter(username=username).exists():
            context['错误'] = '用户已存在'
            return render(request,'blog/regist.html',context)
        else:
            if password == password1:
                password = make_password(password)
                User.objects.create(username=username,password=password)
                user = User.objects.get(username=username)
                cookie = ''
                for i in range(15):
                    s = 'abcdefghijklmnopqrstuvwxyz'
                    cookie += random.choice(s)
                now_time = int(time.time())
                cookie = 'cookie' + cookie + str(now_time)
                response = redirect('index')
                response.set_cookie('cookie', cookie, max_age=10000)
                user.cookie = cookie
                user.save()
                return response
            else:
                context['错误'] = '二次密码不正确'
                return render(request, 'blog/regist.html', context)
    return render(request,'blog/regist.html',context)


def login(request):
    context = {}
    context['分类'] = Type.objects.all()
    if request.method == 'POST':
        username = request.POST['用户名']
        password = request.POST['密码']
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                cookie = ''
                for i in range(15):
                    s = 'abcdefghijklmnopqrstuvwxyz'
                    cookie += random.choice(s)
                now_time = int(time.time())
                cookie = 'cookie' + cookie + str(now_time)
                response = redirect('index')
                response.set_cookie('cookie', cookie, max_age=10000)
                user.cookie = cookie
                user.save()
                return response
            else:
                context['错误'] = '密码错误'
                return render(request, 'blog/login.html', context)
        else:
            context['错误'] = '用户名不存在'
            return render(request, 'blog/login.html', context)

    return render(request,'blog/login.html',context)



def logout(request):
    if request.method == 'GET':
        response = redirect('index')
        response.delete_cookie('cookie')
        return response

def blog_list(request):
    blog_all_list = Article.objects.all()
    paginator = Paginator(blog_all_list,10)
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num)

    context = {}
    context['blog'] = page_of_blogs
    context['分类'] = Type.objects.all()
    context['all'] = Article.objects.all()
    if checkcookie(request, User) is True:
        context['判断'] = True
        cookie = request.COOKIES.get('cookie')
        context['user'] = User.objects.get(cookie=cookie).username
        return render(request, 'blog/blog_list.html', context)
    else:
        return render(request, 'blog/blog_list.html', context)


def blog_detail(request,id):
    context = {}
    context['分类'] = Type.objects.all()
    context['bolg'] = Article.objects.get(id=id)
    if checkcookie(request, User) is True:
        context['判断'] = True
        cookie = request.COOKIES.get('cookie')
        context['user'] = User.objects.get(cookie=cookie).username
        return render(request, 'blog/blog_detail.html', context)
    else:
        return render(request, 'blog/blog_detail.html', context)
