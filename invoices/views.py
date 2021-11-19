from django.shortcuts import render
from products.models import Products
from master.models import Company
from customers.models import Customers
from django.core import serializers

# Create your views here.

def generateinvoice(request):
    productdata = Products.objects.all()
    product = serializers.serialize('json', productdata)

    company = Company.objects.first()

    customer = Customers.objects.all()
    custdata = serializers.serialize('json', customer)
    return render(request,'generateinvoicer2.html',{"productdata":product ,"selectproduct":productdata , "companydata":company, "customerdata":customer, "custdata":custdata})

def invoiceprint(request):
    return render(request,'invoiceprint.html')
