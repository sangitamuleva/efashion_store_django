from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
# Create your views here.

from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('index')



    def get(self , request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        categories=Category.objects.all()
        category_id= request.GET.get('category')

        if category_id:       
            products=Product.objects.filter(category=category_id)
        else:
            products=Product.objects.all()


        context={'products':products,'categories':categories}
        return render(request,'index.html',context)