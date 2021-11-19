from django.shortcuts import render
from .models import Vendors
from django.contrib import messages
from .forms import Updatevendorforms


# Create your views here.

def addvendor(request):
   
    if request.method=="POST":
        if request.POST.get('vendor_name') and request.POST.get('company_name') and request.POST.get('address') and request.POST.get('phno') and request.POST.get('emailid'):
            saverecord = Vendors()
            saverecord.vendor_name=request.POST.get('vendor_name')
            saverecord.company_name=request.POST.get('company_name')
            saverecord.address= request.POST.get('address')
            saverecord.phno = request.POST.get('phno')
            saverecord.emailid = request.POST.get('emailid')
            saverecord.save()

            print('record saved succesfully!')
            messages.success(request,"Vendor " + saverecord.vendor_name + ' Added Successfully!')
            return render(request,'addvendor.html')
        else:
            messages.success(request,'Failed!!! Please Enter Data Properly!')
            return render(request,'addvendor.html')
    else:
        return render(request, 'addvendor.html')

def managevendors(request):
    showall = Vendors.objects.all()
    return render(request,'managevendors.html',{"vendordata":showall})

def EditVendor(request,id):
    editvendorobj= Vendors.objects.get(id = id)
    return render(request,'editvendor.html', {"Vendor":editvendorobj})

def UpdateVendor(request,id):
   UpdateVendor = Vendors.objects.get(id = id) 
   form=Updatevendorforms(request.POST, instance=UpdateVendor)
   if form.is_valid():
       form.save()
       messages.success(request,'Record Updated Successfully!')
       return render(request, 'editvendor.html',{"Vendor":UpdateVendor})

def DelVendor(request,id):
    delvendorobj = Vendors.objects.get(id = id)
    delvendorobj.delete()
    showdata = Vendors.objects.all()
    return render(request,'managevendors.html',{"vendordata":showdata})    