from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import AuctionListForm
from .models import User, AuctionList,Watchlist
from django.utils import timezone







def index(request):
    auctions = AuctionList.objects.all()
    return render(request, "auctions/index.html",{'auctions':auctions})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    forms = AuctionListForm()
    if request.method == "POST":
        form = AuctionListForm(request.POST,request.FILES)
        if form.is_valid():
            image= form.cleaned_data['image']
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            desc = form.cleaned_data['description']
            user = request.user
            auction = AuctionList(user=user,product_image=image,product_name=name,product_description=desc,startin_bid=price,date_created=timezone.now())
            auction.save()
            return redirect('index')
        else:
            return render(request,'auctions/create_listing.html',{'forms':forms})        
    return render(request,'auctions/create_listing.html',{'forms':forms})


# def listing(request,id):
#     auction = AuctionList.objects.get(id=id)
#     all_watch = Watchlist.objects.values_list('name', flat=True)
#     if request.method =="POST":
#         name = AuctionList.objects.get(pk=id).product_name
#         # if name in all_watch:
#         #     # Item is in watchlist, remove it
#         #     Watchlist.objects.filter(name=name).delete()
#         # else:
#         watchlist = Watchlist.objects.create( user=request.user)   
#         watchlist.name.add(auction)
#     msg = " Added to watch List"
#     return render(request, "auctions/listing.html",{'auction':auction,'msg':msg,'all_watch':all_watch,'auction':auction})

def listing(request, id):
    auction = get_object_or_404(AuctionList, id=id)
    print(auction.product_name)
    all_watch =Watchlist.objects.values_list('name', flat=True)
    print(all_watch)
    msg =None
    if request.method == "POST":
        name = auction.product_name
        if name in all_watch:

            Watchlist.objects.filter(name=name).delete()
            

        else:
            msg = "added to watch list"
            Watchlist.objects.create(name=AuctionList.objects.get(id=id).product_name,user=request.user)
            

        
    #     # Check if the auction is already in the watchlist
    #     if not Watchlist.objects.filter(user=request.user, name=auction.product_name).exists():

    #         watchlist.products.add(auction)
    #         msg = f"{auction.product_name} added to watchlist"
    #     else:
    #         msg = f"{auction.product_name} is already in your watchlist"

    return render(request, "auctions/listing.html", {'auction': auction ,"msg":msg})

def watch_list(request):        
    return render(request, 'auctions/watch_list.html')
