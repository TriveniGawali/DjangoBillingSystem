from django.shortcuts import render
from products.models import Products
from django.contrib import messages
from products.forms import Updateproductforms

# Create your views here.

def addproduct(request):
   
    if request.method=="POST":
        if request.POST.get('product_name') and request.POST.get('product_type') and request.POST.get('product_sgst') and request.POST.get('product_cgst') and request.POST.get('product_igst') and request.POST.get('product_desc') and request.POST.get('product_price'):
            saverecord = Products()
            saverecord.product_name=request.POST.get('product_name')
            saverecord.product_type= request.POST.get('product_type')
            saverecord.product_sgst = request.POST.get('product_sgst')
            saverecord.product_cgst = request.POST.get('product_cgst')
            saverecord.product_igst = request.POST.get('product_igst')
            saverecord.product_desc = request.POST.get('product_desc')
            saverecord.product_price = request.POST.get('product_price')
            saverecord.save()

            print('record saved succesfully!')
            messages.success(request,"Product " + saverecord.product_name + ' Added Successfully!')
            return render(request,'addproduct.html')
        else:
            messages.success(request,'Failed!!! Please Enter Data Properly!')
            return render(request,'addproduct.html')
    else:
        return render(request, 'addproduct.html')

def manageproducts(request):
    showall = Products.objects.all()
    return render(request,'manageproducts.html',{"productsdata":showall})

def EditProduct(request,id):
    editproductobj= Products.objects.get(id = id)
    return render(request,'editproduct.html', {"Product":editproductobj})

def UpdateProduct(request,id):
   UpdateProduct = Products.objects.get(id = id) 
   form=Updateproductforms(request.POST, instance=UpdateProduct)
   if form.is_valid():
       form.save()
       messages.success(request,'Record Updated Successfully!')
       return render(request, 'editproduct.html',{"Product":UpdateProduct})

def DelProduct(request,id):
    delproductobj = Products.objects.get(id = id)
    delproductobj.delete()
    showdata = Products.objects.all()
    return render(request,'manageproducts.html',{"productsdata":showdata})    