
from django.urls import path,include
from .views import signup,login,index,cart,checkout,order,home
from store.middleware.auth import auth_middleware
urlpatterns = [
         path('',home.home,name='home'),
         path('contact/',home.contact,name='contact'),
         path('about_us/',home.about_us,name='about_us'),
       path('shop/',index.Index.as_view(),name='index'),
       path('signup/',signup.Signup.as_view(),name='signup'),
       path('login/',login.Login.as_view(),name='login'),
       path('logout/',login.logout,name='logout'),
       path('cart/',cart.Cart.as_view(),name='cart'),
        path('checkout/',checkout.Checkout.as_view(),name='checkout'),
        path('order/',auth_middleware(order.OrderView.as_view()),name='order'),
]
