from django.shortcuts import render

# Create your views here.


from App.models import Nav, Mustbuy, Wheel


def home(request):

    navs = Nav.objects.all()



    mustbuys = Mustbuy.objects.all()



    wheels = Wheel.objects.all()
    data = {
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
    }

    return render(request,'home/home.html',context= data)


def market(request):
    return render(request,'market/market.html')


def mine(request):
    return render(request,'mine/mine.html')


def cart(request):
    return render(request,'cart/cart.html')