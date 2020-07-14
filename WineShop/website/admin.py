from django.contrib import admin

# Register your models here.
from .models import products,orders

admin.site.register(products)
admin.site.register(orders)
