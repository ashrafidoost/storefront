from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product

# Create your views here.
#----------------------------- VIEWS (Mosh)
# Request -> Response
# Other jargons for Views : Request Handler, Action

def first_page(request):
    return HttpResponse('This is the first page of the Store Front')

def say_hello(request):

    product = Product.objects.order_by('unit_price')
    #product = Product.objects.latest('unit_price')

    print(product)

    return render(request, 'hello.html', {'name': 'Reza', 'products': product})
