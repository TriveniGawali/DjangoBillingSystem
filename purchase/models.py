from django.db import models

# Create your models here.

class PurchaseOrders(models.Model):
    ven_name = models.CharField(max_length=120)
    com_name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=100)
    emailid = models.CharField(max_length=150)
    pur_date = models.DateField()
    pur_time = models.TimeField()
    gross_a = models.IntegerField()
    tax = models.IntegerField()
    invoice_amt = models.IntegerField()


    class Meta:
        db_table ="purchaseorder"

class PurchaseProducts(models.Model):
    purno = models.IntegerField()
    pname = models.CharField(max_length=100)
    pqty = models.IntegerField()
    prate = models.IntegerField()
    ptotalamount = models.IntegerField()

    class Meta:
        db_table = "purchaseproducts"
