"""WineShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.HomeView,name='home'),
    path('products/',views.view_Products,name='products'),
    path('cart/',views.view_Cart,name='cart'),
<<<<<<< HEAD
    path('address',views.AddressView,name='cart'),
    path('checkout/',views.checkoutView,name='cart'),
    path('checkout/checkout_price/',views.checkout_price),
=======
    path('contact/',views.view_Contact,name='contact'),
    path('address/',views.view_Address,name='address'),
    path('orders/',views.view_Orders,name='orders'),
    path('about/',views.view_About,name='about'),
>>>>>>> 7829a31035937307b62a67e2fb31593ef5fb769f
    path('', include('website.urls')),
]
