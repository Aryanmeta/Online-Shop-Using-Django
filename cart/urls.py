from django.urls import path

from .views import cart_detail_view

app_name = 'cart'

urlpatterns = [
    path('', cart_detail_view, name='cart_detail'),
]
