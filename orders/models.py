from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(_('User'), settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    first_name = models.CharField(_('First Name'), max_length=50, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=50, blank=True)
    phone_number = models.CharField(_('Phone Number'), max_length=15)
    address = models.CharField(max_length=700)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
