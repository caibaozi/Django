from django.db import models

# Create your models here.
class User(models.Model):
    username = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=256)


class Wheel(models.Model):
    img = models.CharField(max_length=100)
    class Meta:
        db_table='App_wheel'


class Goods(models.Model):
    img = models.CharField(max_length=100)
    prse = models.IntegerField()
    goodsname = models.CharField(max_length=100)


class Cart(models.Model):
    user = models.ForeignKey(User)
    goods = models.ForeignKey(Goods)
    number = models.IntegerField()
    isselect = models.BooleanField(default=True)