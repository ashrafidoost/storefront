from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'last_update', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    #ordering = ['title', 'unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'LOW'
        else:
            return 'OK'
        

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders_count']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name', 'email']
    list_per_page = 10

    @admin.display(ordering='orders_count')
    def orders_count(self, customer):
        url = reverse('admin:store_order_changelist') + '?' + urlencode({'customer__id': customer.id})
        return format_html('<a href="{}" target=_blank>{}</a>', url, customer.order_count)      

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(order_count = Count('order'))


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['payment_status', 'customer_name']
    ordering = ['payment_status']
    list_per_page = 10

    def customer_name(self, order):
        return order.customer.first_name+' '+ order.customer.last_name

    @admin.display(ordering='payment_status')
    def payment_stat(self, order):
        if order.payment_status == 'C':
            return 'COMP'
        else:
            return 'NOMP'


# Register your models here.
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = reverse('admin:store_product_changelist') + '?' + urlencode({'collection__id': collection.id})
        return format_html('<a href="{}" target=_blank>{}</a>', url, collection.products_count)      

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count = Count('product'))