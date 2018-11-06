from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import Wheel, User


def index(request):
    wheels = Wheel.objects.all()
    return render(request, 'index.html', context={'wheel': wheels})



def cart(request):
    return render(request,'cart.html')


def list(request):
    if request.method == 'GET':
        return render(request,'load.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        users = User.objects.filter(username=username).filter(password=password)
        if users.count():
            user = users.first()
            response = redirect('jlg:index')

            response.set_cookie('username',user.user.username)
            return response
        else:
            return HttpResponse('用户木或者密码错误！')







def load(request):
    return render(request,'load.html')


def product(request):
    return render(request,'product.html')


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