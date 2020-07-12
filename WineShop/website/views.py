from django.shortcuts import render
from .models import products
import copy
# Create your views here.

def HomeView(request):
    return render(request, './home.html')

def view_Products(request):
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

    return render(request, './view_Products.html',context)

def view_Cart(request):
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
    context={'data':dict1}
    return render(request,'./view_Cart.html', context)

def view_Contact(request):
    context = {}
    return render(request,'./view_Contact.html', context)

def view_Address(request):
    context = {}
    return render(request,'./address.html', context)

def view_Orders(request):
    context = {}
    return render(request,'./view_Orders.html', context)

def view_About(request):
    context = {}
    return render(request,'./view_About.html', context)
