from django.db import models

# Create your models here.

class Customers(models.Model):
    cust_name = models.CharField(max_length=100)
    cust_address = models.CharField(max_length=100)
    cust_phno = models.CharField(max_length=50)
    cust_email = models.EmailField(max_length=200)
    

    class Meta:
        db_table ="customers"