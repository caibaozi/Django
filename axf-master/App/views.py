from django.shortcuts import render

# Create your views here.


from App.models import Nav, Mustbuy, Wheel, Shop, MainShow, Foodtypes, Goods


def home(request):

    navs = Nav.objects.all()



    mustbuys = Mustbuy.objects.all()



    wheels = Wheel.objects.all()

    shop = Shop.objects.all()
    shophead = shop[0]
    shoptab = shop[1:3]
    shopclass = shop[3:7]
    shopcommend = shop[7:11]



    mainshows = MainShow.objects.all()




    data = {
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead':shophead,
        'shoptab':shoptab,
        'shopclass':shopclass,
        'shopcommend':shopcommend,
        'mainshows':mainshows
    }

    return render(request,'home/home.html',context= data)


def market(request,categoryid):

    foodtypes = Foodtypes.objects.all()
    # goodsList = Goods.objects.all()[0:5]
    goodsList = Goods.objects.filter(categoryid=categoryid)
    data = {
        'foodtypes':foodtypes,
        'goodsList':goodsList
    }

    return render(request,'market/market.html',context=data)


def mine(request):
    return render(request,'mine/mine.html')


def cart(request):
    return render(request,'cart/cart.html')


def registe(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    return render(request,'mine/registe.html')