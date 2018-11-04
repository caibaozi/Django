from django.shortcuts import render

# Create your views here.
from App.models import Wheel


def index(request):
    wheels = Wheel.objects.all()
    return render(request, 'index.html', context={'wheel': wheels})



def cart(request):
    return render(request,'cart.html')


def list(request):
    return render(request,'list.html')


def load(request):
    return render(request,'load.html')


def product(request):
    return render(request,'product.html')


def register(request):
    return render(request,'register.html')