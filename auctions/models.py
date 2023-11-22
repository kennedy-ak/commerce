from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    location = models.CharField(max_length=50,default=True,null=True)

    def __str__(self):
        return f"{self.username}"
    
class AuctionList(models.Model):

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_image = models.ImageField(null=True,blank=True, upload_to="images/")
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=100,blank=True, null=True)
    startin_bid = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.product_name}"
    



class Bids(models.Model):
    pass


class Comments(models.Model):
    pass


class Watchlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    name = models.ManyToManyField(AuctionList,blank=True,null=True)
    hellp

    def __str__(self):
        return self.user.username
    