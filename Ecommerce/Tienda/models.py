from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
from uuidfield import UUIDField


class ClientModel(models.Model):
	idClient = UUIDField(primary_key=True, auto=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class ProductModel(models.Model):
	idProducto = UUIDField(primary_key=True, auto=False)
	title = models.CharField(max_length=100)
	description = models.TextField()
	price = models.FloatField()
	discount_price = models.FloatField(blank=True, null=True)
	category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
	image = models.ImageField()
	slug = models.SlugField()
	label = models.CharField(choices=LABEL_CHOICES, max_length=1)

	def __str__(self):
        return self.title


class OrderModel(models.Model):
	idClient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	idProducto = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
	payment = models.FloatField()
	state = models.CharField(max_length=20, blank=True, null=True)
	ordered_date = models.DateTimeField()

