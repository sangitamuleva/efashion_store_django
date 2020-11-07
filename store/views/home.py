from django.shortcuts import render,redirect,HttpResponseRedirect
# Create your views here.

from django.views import View


# Create your views here.


def home(request):
        context={}
        return render(request,'home.html',context)

def contact(request):
        context={}
        return render(request,'contact.html',context)

def about_us(request):
        context={}
        return render(request,'about_us.html',context)