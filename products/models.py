from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    product_sgst = models.CharField(max_length=30)
    product_cgst = models.CharField(max_length=30)
    product_igst = models.CharField(max_length=30)
    product_desc = models.CharField(max_length=100)
    product_price = models.IntegerField()

    class Meta:
        db_table ="products"