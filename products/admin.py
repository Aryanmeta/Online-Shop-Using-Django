from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Product, Comment


class CommentsInLine(admin.TabularInline):  # class CommentsInLine(admin.StackedInline):
    model = Comment
    # readonly_fields = ['author', 'body', 'starts', 'active', ]
    fields = ['author', 'body', 'starts', 'active', ]
    raw_id_fields = ['author', ]
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'datetime_created', ]

    inlines = [
        CommentsInLine,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'starts', 'datetime_created', 'active', ]
