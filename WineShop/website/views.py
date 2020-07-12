from django.shortcuts import render
from .models import products
import copy
import json
from django.http import JsonResponse
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


def AddressView(request):
    return render(request, './address.html')

def checkoutView(request):

    items= products.objects.all()
    list1=[]
    dict1={}
    list2=[]
    for i in items:
        #print(i.name,' ',i.price,' ',i.category)
        list1.append(i.name)
        list1.append(i.price)
        list1.append(i.category)
        list1.append(i.quantity)
        list2 = copy.deepcopy(list1)
        dict1[i.id] = list2

        list1.clear()
    #print(dict1)
    context={'data_items':dict1}
    return render(request,'./checkout.html')

def checkout_price(request):
    post_id = request.GET['items']
    dict1=post_id
    res = json.loads(post_id)
    print('inside ajax views')
    print("dictionary print ",dict1)
    print(res)
    total_price=0
    grand_total=0

    list1=[]

    list2=[]
    dict1={}
    for i,j in res.items():
        print(i)
    print(type(res))
    total_price=0
    for i,j in res.items():
        items=products.objects.filter(pk=i)
        price=0


        print("id: ",i," quantity: ",j)
        for k in items:
            #print(k.name)
            #print(k.price)
            #print(k.quantity)
            #print(k.category)
            #price=k.price*j
            #print('price of ',k.name,' quantity: ',price)

            price=k.price*j
            list1.append(k.name)
            list1.append(k.category)
            list1.append(k.price)
            list1.append(k.quantity)
            list1.append(j)
            #list1.append(i.id)
            list1.append(price)
            #print("ml - ",k.quantity)
            #print("total -", total_price)
            total_price+=price
            list2 = copy.deepcopy(list1)
            dict1[i]=list2
            print(dict1)
            list1.clear()
    print("total price ",total_price)
    context={
    'data':dict1,
    'grand_total':total_price
    }
    print(context)
    return JsonResponse(context)
    #return render(request,'./checkout_2.html',context)

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

def view_Disclaimer(request):
    context = {}
    return render(request,'./view_Disclaimer.html', context)
