from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(_('Product Title'), max_length=100, blank=True)
    description = RichTextField(_('Product Description'), blank=True)
    short_description = models.CharField(_('Product Short Description'), max_length=300, blank=True)
    price = models.PositiveIntegerField(_('Product Price'), default=0, blank=True)
    active = models.BooleanField(_('Product Display'), default=True, blank=True)
    image = models.ImageField(_('Product Image'), upload_to='product/product_cover/', blank=True)

    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


# class ActiveCommentManager(models.Manager):
#     def get_queryset(self):
#         return super(ActiveCommentManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',
                                verbose_name=_('Product Choice'))
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('Author Comment'))
    body = models.TextField(_('Comment'))
    starts = models.CharField(_('your star'), max_length=10, choices=PRODUCT_STARS)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(_('Comment Display'), default=True)

    # # Manager
    # objects = models.Manager
    # active_comments_manager = ActiveCommentManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
