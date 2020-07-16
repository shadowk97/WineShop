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
from WineShop import settings
from django.conf.urls.static import static
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView,name='home'),
    path('home/',views.HomeView,name='home'),
    #path('products/',views.view_Products,name='products'),
    ###################
    path('products/',views.view_new_products,name='products'),
    path('products/whiskey/',views.view_Whiskey,name='whiskey'),
    path('products/wine/',views.view_Wine,name='wine'),
    path('products/vodka/',views.view_Vodka,name='vodka'),
    path('products/beers/',views.view_Beers,name='beers'),
    path('products/spirits/',views.view_Spirits,name='spirits'),
    ####################
    path('checkout/',views.checkoutView,name='cart'),
    path('checkout/checkout_price/',views.checkout_price),
    path('address/',views.view_Address,name='address'),
    path('about/',views.view_About,name='about'),
    path('disclaimer/',views.view_Disclaimer,name='disclaimer'),
    path('cart/',views.lol,name='lol'),
    path('cart/final_checkout',views.final_checkout,name='final_checkout'),
    path('', include('website.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
