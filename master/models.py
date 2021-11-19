from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    gstin = models.CharField(max_length=50)
    addr=models.CharField(max_length=300)
    mobile = models.CharField(max_length=100)
    email=models.EmailField()
    website=models.URLField()
    industry=models.CharField(max_length=100)
    logoimg = models.ImageField(upload_to='pics')
    

   