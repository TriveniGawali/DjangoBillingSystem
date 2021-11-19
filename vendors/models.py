from django.db import models

# Create your models here.

class Vendors(models.Model):
    vendor_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phno = models.CharField(max_length=50)
    emailid = models.EmailField(max_length=200)
    

    class Meta:
        db_table ="vendors"