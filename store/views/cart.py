from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import  View

class Cart(View):
    return_url = None
    def get(self , request):
        ids=list(request.session.get('cart').keys())
        product=Product.objects.filter(id__in=ids)
        context={'products':product}
        return render(request , 'cart.html',context)

    
