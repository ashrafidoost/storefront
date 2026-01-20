from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.
#----------------------------- VIEWS (Mosh)
# Request -> Response
# Other jargons for Views : Request Handler, Action

def first_page(request):
    return HttpResponse('This is the first page of the Store Front')

def say_hello(request):
    query_set = Product.objects.get(pk=1)

    print(query_set)

    return render(request, 'hello.html', {'name': 'Reza'})
