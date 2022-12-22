from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price', ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'phone_number', 'address', 'order_note',
                    'datetime_created', 'datetime_modified', 'is_paid', ]

    inlines = [
        OrderItemInLine,
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', ]
