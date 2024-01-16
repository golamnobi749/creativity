from django.contrib import admin
from .models import Product,Customer,Cart,OrderPlace

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','product_name', 'price','courrent_price','meta_title','brand','category','created_date','image')
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user','name','email','phone','address','city','house_building','zipcode')
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display =('customer', 'products','quantity','total_amount')
@admin.register(OrderPlace)
class OrderPlaceAdmin(admin.ModelAdmin):
    list_display = ('cart','product','customer','status','quantity','location','order_date')
