from django.contrib import admin
from . models import Products,Category,Customer
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ('name','price','category',)
    search_fields = ('name','price',)
    list_filter = ('name','price',)

class ProductCategory(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class CustomerName(admin.ModelAdmin):
    list_display = ('first_name',)
    
    
admin.site.register(Products,AdminProduct)
admin.site.register(Category,ProductCategory)
admin.site.register(Customer,CustomerName)