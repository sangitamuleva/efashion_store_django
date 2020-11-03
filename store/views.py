from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
# Create your views here.
def index(request):
    
    categories=Category.objects.all()
    category_id= request.GET.get('category')

    if category_id:       
        products=Product.objects.filter(category=category_id)
    else:
        products=Product.objects.all()


    context={'products':products,'categories':categories}
    return render(request,'index.html',context)

def signup(request):
    context={}
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        # validations
        error_message=None

        customer=Customer(first_name=first_name,
                                last_name=last_name,
                                email=email,
                                phone=phone,
                                password=password)

        if (not first_name):
            error_message = "First Name Required !!"
        elif len(first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not last_name:
            error_message = 'Last Name Required'
        elif len(last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not phone:
            error_message = 'Phone Number required'
        elif len(phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(password) < 6:
            error_message = 'Password must be 6 char long'
       
        elif customer.check_email_exist():
            error_message = 'Email Address Already Registered..'
        if not error_message:    
                customer.password=make_password(customer.password)            
                customer.save()
                
                return redirect(index)
        else :
            context['error']=error_message
            context['values']= value
            return render(request,'signup.html',context)
    
    return render(request,'signup.html',context)

def login(request):
    context={}
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        customer=Customer.get_customer_by_email(email)
        print(customer.password)
        error_message=None

        if customer:
            password_flag=check_password(password,customer.password)
           
            if password_flag:
                return redirect('index')
            else:
                error_message='Email or Password incorrect !!'
        else:
            error_message='Email or Password incorrect !!'

        print(customer)
        context['error']=error_message
        return render(request,'login.html',context)
    
    return render(request,'login.html',context)