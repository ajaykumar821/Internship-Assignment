
from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)

class Buyer(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)

class InvoiceItem(models.Model):
    product = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_number = models.CharField(max_length=10)
    invoice_date = models.DateField()
