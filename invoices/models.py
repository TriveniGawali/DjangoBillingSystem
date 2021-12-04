from django.db import models

# Create your models here.

class Orders(models.Model):
    cust_name = models.CharField(max_length=150)
    cust_addr = models.CharField(max_length=150)
    cust_phno = models.CharField(max_length=50)
    cust_email = models.CharField(max_length=150)
    order_date = models.DateField()
    order_time = models.TimeField()
    gross_amt = models.IntegerField()
    discount = models.IntegerField()
    net_amt = models.IntegerField()


    class Meta:
        db_table ="orders"

class OrderProduct(models.Model):
    orderno = models.IntegerField()
    productname = models.CharField(max_length=100)
    qty = models.IntegerField()
    rate = models.IntegerField()
    total = models.IntegerField()
    cgst = models.IntegerField()
    sgst = models.IntegerField()
    igst = models.IntegerField(null = True)
    totalamount = models.IntegerField()

    class Meta:
        db_table = "orderproduct"