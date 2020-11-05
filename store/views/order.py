from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.order import Order
from django.views import  View
from store.middleware.auth import auth_middleware
from django.utils.decorators import method_decorator


class OrderView(View):
    return_url = None
   
    def get(self , request):
        customer=request.session.get('customer')
        order=Order.objects.filter(customer=customer).order_by('date')
        context={'orders':order}
        return render(request , 'orders.html',context)

    
