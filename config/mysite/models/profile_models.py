from .account_models import models
from django.contrib.auth import get_user_model

class Profile(models.Model):

    user = models.OneToOneField(get_user_model(),unique=True,on_delete=models.CASCADE,primary_key=True)


    username = models.CharField(default="匿名ユーザー",max_length=100)

    zipcode = models.CharField(max_length=30,default="")

    prefecture = models.CharField(max_length=6,default="")

    city = models.CharField(max_length=100,default="")

    address = models.CharField(max_length=200,default="")