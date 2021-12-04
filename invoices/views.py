from django.shortcuts import redirect, render
from products.models import Products
from master.models import Company
from customers.models import Customers
from django.core import serializers
from .models import OrderProduct, Orders
from django.contrib import messages
from django.forms import formset_factory

# Create your views here.

def generateinvoice(request):
    productdata = Products.objects.all()
    product = serializers.serialize('json', productdata)

    company = Company.objects.first()

    customer = Customers.objects.all()
    custdata = serializers.serialize('json', customer)

    order = Orders.objects.all()
    orderdata = serializers.serialize('json', order)

    return render(request,'generateinvoicer2.html',{"productdata":product ,"selectproduct":productdata , "companydata":company, "customerdata":customer, "custdata":custdata, "orderdata":order, "orderdataj": orderdata})

def printinvoice(request,id):
    company = Company.objects.first()
    printinvoiceobj = Orders.objects.get(id = id)
    printinvoiceprodobj = OrderProduct.objects.filter(orderno = id)
    print(printinvoiceprodobj)
    return render(request,'printinvoice.html',{"companydata":company, "printorderdata":printinvoiceobj, "printproddata": printinvoiceprodobj })

def manageinvoices(request):
   showall = Orders.objects.all()
   return render(request,'manageinvoices.html',{"invoicedata":showall}) 

def DelInvoice(request,id):
    delinvoiceobj = Orders.objects.get(id = id)
    delinvoiceobj.delete()
    delinvoiceprodobj = OrderProduct.objects.filter(orderno = id)
    for i in delinvoiceprodobj:
        i.delete()
    showdata = Orders.objects.all()
    return render(request,'manageinvoices.html',{"invoicedata":showdata})    


def billsaved(request):
    return render(request, 'billsaved.html')

def savebillproducts(request):
   
    productdata = Products.objects.all()
    product = serializers.serialize('json', productdata)

    company = Company.objects.first()

    customer = Customers.objects.all()
    custdata = serializers.serialize('json', customer)

    order = Orders.objects.all()
    orderdata = serializers.serialize('json', order)

    if request.method=="POST":
        if  request.POST.get('cust_name') and request.POST.get('cust_addr') and request.POST.get('cust_phno') and request.POST.get('cust_email') and request.POST.get('order_date') and request.POST.get('order_time') and request.POST.get('gross_amt') and request.POST.get('discount') and request.POST.get('net_amt') and request.POST.get('tablerowcnt') and request.POST.get('orderno') and request.POST.get('product_ar') and request.POST.get('qty_ar') and request.POST.get('rate_ar') and request.POST.get('total_ar') and request.POST.get('cgst_ar') and request.POST.get('sgst_ar') and request.POST.get('igst_ar') and request.POST.get('totalamount_ar'):
           
            saverecordc = Orders()
            saverecordc.cust_name=request.POST.get('cust_name')
            saverecordc.cust_addr= request.POST.get('cust_addr')
            saverecordc.cust_phno = request.POST.get('cust_phno')
            saverecordc.cust_email = request.POST.get('cust_email')
            saverecordc.order_date = request.POST.get('order_date')
            saverecordc.order_time = request.POST.get('order_time')
            saverecordc.gross_amt = request.POST.get('gross_amt')
            saverecordc.discount = request.POST.get('discount')
            saverecordc.net_amt = request.POST.get('net_amt')
            saverecordc.save()

            tc = int(request.POST.get('tablerowcnt'))+ 1
            pa = (request.POST.get('product_ar')).split(';')
            qa = (request.POST.get('qty_ar')).split(';')
            ra = (request.POST.get('rate_ar')).split(';')
            ta  = (request.POST.get('total_ar')).split(';')
            ca = (request.POST.get('cgst_ar')).split(';')
            sa = (request.POST.get('sgst_ar')).split(';')
            ia = (request.POST.get('igst_ar')).split(';')
            taa = (request.POST.get('totalamount_ar')).split(';')
            
            for i in range(1,tc):
                saverecord = OrderProduct()
                saverecord.orderno = request.POST.get('orderno')
                saverecord.productname= pa[i]
                saverecord.qty = qa[i]
                saverecord.rate = ra[i]
                saverecord.total = ta[i]
                saverecord.cgst = ca[i]
                saverecord.sgst = sa[i]
                saverecord.igst = ia[i]
                saverecord.totalamount = taa[i]
                saverecord.save()
            
            print('record saved succesfully!')
            messages.success(request,'Order Added Successfully!')
            return render(request,'generateinvoicer2.html',{"productdata":product ,"selectproduct":productdata , "companydata":company, "customerdata":customer, "custdata":custdata, "orderdata":order, "orderdataj": orderdata})
        else:
            messages.success(request,'Failed to add your Order!!! Please Enter Data Properly!')
            return render(request,'generateinvoicer2.html',{"productdata":product ,"selectproduct":productdata , "companydata":company, "customerdata":customer, "custdata":custdata, "orderdata":order, "orderdataj": orderdata})
    else:
        return render(request, 'generateinvoicer2.html',{"productdata":product ,"selectproduct":productdata , "companydata":company, "customerdata":customer, "custdata":custdata, "orderdata":order, "orderdataj": orderdata})



        
        
        
        
        
        
        
        
        
        
       