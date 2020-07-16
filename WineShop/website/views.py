from django.shortcuts import render
from .models import products,orders
import copy
import json
from django.http import JsonResponse
# Create your views here.
data_cart={}
data_total=0
def HomeView(request):
    return render(request, './home.html')

#def view_Products(request):
#    items= products.objects.all()
#    list1=[]
#    dict1={}
#    list2=[]
#    for i in items:
#        print(i.name,' ',i.price,' ',i.category)
#        list1.append(i.name)
#        list1.append(i.price)
#        list1.append(i.category)
#        list1.append(i.quantity)
#        list2 = copy.deepcopy(list1)
#        dict1[i.id] = list2
#
#        list1.clear()
#    print(dict1)
#    context={'data_items':dict1}
#
#    return render(request, './view_Products.html',context)

def checkoutView(request):
    print('inside views')
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
    print(context)
    return render(request,'./checkout.html')

def checkout_price(request):
    print('inside price views')
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
    total_price=total_price+5
    context={
    'data':dict1,
    'grand_total':total_price
    }
    global data_cart
    global data_total
    data_cart=dict1
    data_total=total_price
    print(context)
    print('data from gloal cart- ',data_cart)
    return JsonResponse(context)

def view_Address(request):
    context = {}
    return render(request,'./address.html', context)

def view_About(request):
    context = {

    }
    return render(request,'./view_About.html', context)

def view_Disclaimer(request):
    context = {}
    return render(request,'./view_Disclaimer.html', context)

def lol(request):
    global data_cart
    global data_total
    print('inside lol')
    print('data in gloal cart: ',data_cart)
    context={'data':data_cart,
    'grand_total':data_total}
    print(context)
    return render(request,'./lol.html',context)

def final_checkout(request):
    global data_cart
    cart = data_cart
    user = request.GET['details']
    import random
    id = 0
    query = orders.objects.filter(oid=id)
    oid = 0
    while True:
        oid = random.randint(1,10000)
        if not query:
            break
    context = {
        'oid':oid,
    }
    from decimal import Decimal
    new_cart = ""
    for i in cart.keys():
        fl = 0
        for j in cart[i]:
            if fl == 0:
                new_cart += "Item Name : " + str(j) + "\n"
            elif fl == 1:
                new_cart += "Category : " + str(j) + "\n"
            elif fl == 2:
                new_cart += "Price : " + str(j) + "\n"
            elif fl == 3:
                new_cart += "Qty : " + str(j) + " ml\n"
            elif fl == 4:
                new_cart += "Quantity : " + str(j) + "\n"
            elif fl == 5:
                new_cart += "Total : Rs " + str(j) + "\n"
            fl += 1
        new_cart += "\n"

    global data_total

    new_cart += "Grand Total : " + str(data_total) + "\n\n";

    # DB Entry
    print('Cart ' + new_cart)
    print('User ', user)
    order1=orders()
    order1.oid=oid
    order1.cart=new_cart
    order1.user=str(user)
    order1.save()
    print("\n\nOID : ", oid, "\n\n")
    # Send Email
    #import smtplib
    #server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    #server.login("shivamwines123@gmail.com","9892594870")
    #mail_string = "Hi, new order " + str(oid) + " has been placed.\n" + new_cart + "\n" + str(user);
    #server.sendmail("shivamwines123@gmail.com","maxhiren@gmail.com",mail_string)
    #server.quit()

    #Clear Cart
    #data_cart = {}
    return JsonResponse(context)

def view_new_products(request):
    context = {}
    return render(request,'./products.html',context)

def view_Whiskey(request):
    items= products.objects.filter(category='whiskey')
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

def view_Vodka(request):
    items= products.objects.filter(category='vodka')
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

def view_Wine(request):
    items= products.objects.filter(category='wine')
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

def view_Beers(request):
    items= products.objects.filter(category='beer')
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

def view_Spirits(request):
    items= products.objects.filter(category='spirits')
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
