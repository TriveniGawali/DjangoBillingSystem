from django.shortcuts import render
from vendors.models import Vendors
from products.models import Products
from django.core import serializers
from .models import PurchaseOrders, PurchaseProducts
from django.contrib import messages

# Create your views here.


def newpurchase(request):
    productdata = Products.objects.all()
    product = serializers.serialize('json', productdata)

    vendor = Vendors.objects.all()
    vendordata = serializers.serialize('json', vendor)

    purchaseorder = PurchaseOrders.objects.all()
    purchaseorderdata = serializers.serialize('json', purchaseorder)

    return render(request,'newpurchase.html',{"productdata":product ,"selectproduct":productdata , "vendordata":vendor, "vendata":vendordata, "purorderdata":purchaseorder, "purorderdataj": purchaseorderdata})

def savepurchaseorder(request):
    productdata = Products.objects.all()
    product = serializers.serialize('json', productdata)

    vendor = Vendors.objects.all()
    vendordata = serializers.serialize('json', vendor)

    purchaseorder = PurchaseOrders.objects.all()
    purchaseorderdata = serializers.serialize('json', purchaseorder)

    if request.method=="POST":
        if  request.POST.get('ven_name') and request.POST.get('com_name') and request.POST.get('address') and request.POST.get('phone') and request.POST.get('emailid') and request.POST.get('pur_date') and request.POST.get('pur_time') and request.POST.get('gross_a') and request.POST.get('tax') and request.POST.get('invoice_amt') and request.POST.get('tablerowcnt') and request.POST.get('purno') and request.POST.get('pname_ar') and request.POST.get('pqty_ar') and request.POST.get('prate_ar') and request.POST.get('ptotalamount_ar'):
            saverecordv = PurchaseOrders()
            saverecordv.ven_name = request.POST.get('ven_name')
            saverecordv.com_name = request.POST.get('com_name')
            saverecordv.address = request.POST.get('address')
            saverecordv.phone = request.POST.get('phone')
            saverecordv.emailid = request.POST.get('emailid')
            saverecordv.pur_date = request.POST.get('pur_date')
            saverecordv.pur_time = request.POST.get('pur_time')
            saverecordv.gross_a = request.POST.get('gross_a')
            saverecordv.tax = request.POST.get('tax')
            saverecordv.invoice_amt = request.POST.get('invoice_amt')
            saverecordv.save()

            tc = int(request.POST.get('tablerowcnt'))+ 1
            pa = (request.POST.get('pname_ar')).split(';')
            qa = (request.POST.get('pqty_ar')).split(';')
            ra = (request.POST.get('prate_ar')).split(';')
            taa = (request.POST.get('ptotalamount_ar')).split(';')

            for i in range(1,tc):
                saverecord = PurchaseProducts()
                saverecord.purno = request.POST.get('purno')
                saverecord.pname= pa[i]
                saverecord.pqty = qa[i]
                saverecord.prate = ra[i]
                saverecord.ptotalamount = taa[i]
                saverecord.save()


            print('record saved succesfully!')
            messages.success(request,'Order Added Successfully!')
            return render(request,'newpurchase.html' ,{"productdata":product ,"selectproduct":productdata , "vendordata":vendor, "vendata":vendordata, "purorderdata":purchaseorder, "purorderdataj": purchaseorderdata})
        else:
            messages.success(request,'Failed to add your Order!!! Please Enter Data Properly!')
            return render(request,'newpurchase.html' ,{"productdata":product ,"selectproduct":productdata , "vendordata":vendor, "vendata":vendordata, "purorderdata":purchaseorder, "purorderdataj": purchaseorderdata})
    else:
        return render(request, 'newpurchase.html' ,{"productdata":product ,"selectproduct":productdata , "vendordata":vendor, "vendata":vendordata, "purorderdata":purchaseorder, "purorderdataj": purchaseorderdata})

def managepurchase(request):
   showall = PurchaseOrders.objects.all()
   return render(request,'managepurchase.html',{"purchasedata":showall})

def DelPurchase(request,id):
    delpurchaseobj = PurchaseOrders.objects.get(id = id)
    delpurchaseobj.delete()
    delinvoiceprodobj = PurchaseProducts.objects.filter(purno = id)
    for i in delinvoiceprodobj:
        i.delete()
    showdata = PurchaseOrders.objects.all()
    return render(request,'managepurchase.html',{"purchasedata":showdata})    

def printpurchase(request,id):
    printpurchaseobj = PurchaseOrders.objects.get(id = id)
    printpurchaseprodobj = PurchaseProducts.objects.filter(purno = id)
    return render(request,'printpurchase.html',{"printpurchasedata":printpurchaseobj, "printpurproddata": printpurchaseprodobj })
