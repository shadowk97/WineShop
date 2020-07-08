from django.shortcuts import render
from .models import products
import copy

# Create your views here.
def view_products(request):
    items = products.objects.all()
    temp = []
    prods = {}
    temp2 = []
    for i in items:
        temp.append(i.price)
        temp.append(i.name)
        temp.append(i.quantity)
        temp.append(i.category)
        temp2 = copy.deepcopy(temp)
        prods[i.id] = temp2
        print('PRODSSS = ', end="")
        print(prods)
        temp.clear()

    context = {
    'data': prods,
    }
    return render(request,'./products.html', context)
