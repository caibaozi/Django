from django.conf.urls import url

from App import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^list/$',views.list,name='list'),
    url(r'^load/$',views.load,name='load'),
    url(r'^product/$',views.product,name='product'),
    url(r'^register',views.register,name='register')
]