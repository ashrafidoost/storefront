from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Func
from django.db.models.functions import Concat
from django.db.models import Avg, Max, Min, Count, Sum
from django.db.models import Value, ExpressionWrapper, DecimalField
from store.models import Product, OrderItem, Customer, Order

# Create your views here.
#----------------------------- VIEWS (Mosh)
# Request -> Response
# Other jargons for Views : Request Handler, Action

def first_page(request):
    return HttpResponse('This is the first page of the Store Front')

def say_hello(request):

    #query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20) & ~Q(last_update__year__lt=2021))
    #query_set = list(Product.objects.all().order_by('unit_price').filter(last_update__year__lt=2021))[5:15]
    #query_set = Product.objects.values('id', 'title', 'collection__title')
    #query_set = Product.objects.filter(id__in=OrderItem.objects.values('product__id').distinct()).order_by('id', '-title')
    #query_set = Product.objects.prefetch_related('promotions').select_related('collection').all()
    #query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    #query_set = Product.objects.filter(collection__id=3).aggregate(cnt=Count('id'), maximum=Max('unit_price'), minimum=Min('unit_price'), summon=Sum('unit_price'))
    #query_set = Customer.objects.annotate(is_new=Value(True), New_ID=F('id')+10, FullName=Func(F('first_name'), Value(' '), F('last_name'), function='concat'))
    #query_set = Customer.objects.annotate(FullName=Concat('first_name', Value(' '), 'last_name'))
    #query_set = Customer.objects.annotate(orders_count=Count('order'))

    discounted_price = ExpressionWrapper(F('unit_price')*0.8, output_field=DecimalField(max_digits=10, decimal_places=2))
    query_set = Product.objects.annotate(discounted_price = discounted_price)


    #print(query_set)

    return render(request, 'hello.html', {'name': 'Reza', 'products': query_set})
