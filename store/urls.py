
from django.urls import path,include
from .views import signup,login,index,cart

urlpatterns = [
       path('',index.Index.as_view(),name='index'),
       path('signup/',signup.Signup.as_view(),name='signup'),
       path('login/',login.Login.as_view(),name='login'),
       path('logout/',login.logout,name='logout'),
       path('cart/',cart.Cart.as_view(),name='cart'),
]
