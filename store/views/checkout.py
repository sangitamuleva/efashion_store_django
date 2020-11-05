from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.order import Order
from django.views import  View

class Checkout(View):
    
    def post(self , request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.objects.filter(id__in=list(cart.keys()))
        # print(products)

        for p in products:
            order=Order(customer=Customer(id=customer),
            address=address,
            phone=phone,product=p,price=p.price,quantity=cart.get(str(p.id)))
            order.save()

            request.session['cart']={}
        return redirect('cart')

    
