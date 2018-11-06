from django.db import models

# Create your models here.
class User(models.Model):
    username = models.IntegerField(max_length=40,unique=True)
    password = models.CharField(max_length=256)


class Wheel(models.Model):
    img = models.CharField(max_length=100)
    class Meta:
        db_table='App_wheel'