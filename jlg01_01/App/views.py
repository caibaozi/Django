from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import Wheel, User, Goods


def index(request):
    wheels = Wheel.objects.all()
    goods = Goods.objects.all()
    return render(request, 'index.html', context={'wheel': wheels,'goods':goods})



def cart(request,id):
    goods = Goods.objects.filter(id=id).first()
    return render(request,'cart.html',context={'goods':goods})


def list(request):
    return render(request,'list.html')







def load(request):
    if request.method == 'GET':
        return render(request,'load.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        users = User.objects.filter(username=username).filter(password=password)
        if users.count():
            user = users.first()
            response = redirect('jlg:index')
            response.set_cookie('username',user.username)
            return response
        else:
            return HttpResponse('用户名或者密码错误！')


def product(request,id):
    goods = Goods.objects.filter(id=id).first()

    return render(request,'product.html',context={'goods':goods})


def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = User()
        user.username = username
        user.password = password
        user.save()

        response = redirect('jlg:index')
        response.set_cookie('username',username)
    return response