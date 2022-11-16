from django.contrib import admin

from .models import Product, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'datetime_created']


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'starts', 'datetime_created', 'active']
