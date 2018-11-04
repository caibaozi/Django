from django.db import models

# Create your models here.
class Base(models.Model):
    img = models.CharField(max_length=100)

    name = models.CharField(max_length=100)

    trackid = models.CharField(max_length=10)


    class Meta:
        abstract = True

class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'

class Nav(Base):
    class Meta:
        db_table = 'axf_nav'

class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'

class Shop(Base):
    class Meta:
        db_table = 'axf_shop'

        # (trackid, name, img, categoryid, brandname, img1, childcid1, productid1, longname1, price1,
        #              marketprice1, img2, childcid2, productid2, longname2, price2, marketprice2, img3, childcid3,
        #              productid3, longname3, price3, marketprice3)


class MainShow(models.Model):
    trackid = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=8)
    brandname = models.CharField(max_length=50)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=8)
    productid1 = models.CharField(max_length=8)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()


    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=8)
    productid2 = models.CharField(max_length=8)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()


    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=8)
    productid3 = models.CharField(max_length=8)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()



class Foodtypes(models.Model):
    typeid = models.CharField(max_length=8)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=256)
    typesort = models.IntegerField()
    class Meta:
        db_table = 'axf_foodtypes'



# (,,,,,,,,,,,,,,)

class Goods(models.Model):
    productid=models.CharField(max_length=10)
    productimg=models.CharField(max_length=100)
    productname=models.CharField(max_length=100)
    productlongname=models.CharField(max_length=100)
    isxf=models.BooleanField(default=False)
    pmdesc=models.BooleanField(default=False)
    specifics=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    marketprice=models.DecimalField(max_digits=7,decimal_places=2)

    categoryid=models.IntegerField()
    childcid=models.IntegerField()
    childcidname=models.CharField(max_length=100)
    dealerid=models.CharField(max_length=10)
    storenums=models.IntegerField()
    productnum=models.IntegerField()


    class Meta:
        db_table = 'axf_goods'