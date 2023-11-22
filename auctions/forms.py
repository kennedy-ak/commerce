
from django import forms


class AuctionListForm (forms.Form):
    image = forms.ImageField()
    name = forms.CharField(label="Product Name")
    price = forms.CharField(label="Starting Bid")
    description = forms.CharField(label=" Product Description",widget=forms.Textarea())
    