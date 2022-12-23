from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    is_paid = models.BooleanField(_('Finalized ?'), default=False)

    first_name = models.CharField(_('First Name'), max_length=50, blank=False)
    last_name = models.CharField(_('Last Name'), max_length=50, blank=False)
    # An optional phone number.
    # phone_number = PhoneNumberField(_('Phone Number'), blank=True)
    phone_number = models.CharField(_('Phone Number'), max_length=15, blank=False)

    address = models.CharField(_('Address'), max_length=700, blank=False)
    order_note = models.TextField(_('Note'), blank=True)

    datetime_created = models.DateTimeField(_('Created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('Modified'), auto_now=True)

    def __str__(self):
        return f'Order : {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_('Order'))
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items',
                                verbose_name=_('Product'))
    quantity = models.PositiveSmallIntegerField(_('Quantity'), default=1)
    price = models.PositiveIntegerField(_('Product Price'), blank=True)

    def __str__(self):
        return f'OrderItem : {self.id} : {self.product} x {self.quantity} (Price : {self.price})'
