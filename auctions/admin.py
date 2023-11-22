from django.contrib import admin
from .models import User,AuctionList, Watchlist
# Register your models here.
admin.site.register(User)
admin.site.register(AuctionList)
admin.site.register(Watchlist)