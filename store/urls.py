
from django.urls import path,include
from .views import *
urlpatterns = [
       path('',index,name='index'),
       path('signup/',signup,name='signup'),
       path('login/',login,name='login'),
]
