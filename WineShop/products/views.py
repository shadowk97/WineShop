from django.shortcuts import render
from .models import products
import copy

# Create your views here.

def view_Category(request):
    items= products.objects.all()
    list1=[]
    dict1={}
    list2=[]
    for i in items:
        print(i.name,' ',i.price,' ',i.category)
        list1.append(i.name)
        list1.append(i.price)
        list1.append(i.category)
        list1.append(i.quantity)
        list2 = copy.deepcopy(list1)
        dict1[i.id] = list2

        list1.clear()
    print(dict1)
    context={'data_items':dict1}

    return render(request, './view_Category.html',context)
