from django.shortcuts import render
from .models import Customers
from django.contrib import messages
from .forms import Updatecustomerforms

# Create your views here.

def addcustomer(request):
   
    if request.method=="POST":
        if request.POST.get('cust_name') and request.POST.get('cust_address') and request.POST.get('cust_phno') and request.POST.get('cust_email'):
            saverecord = Customers()
            saverecord.cust_name=request.POST.get('cust_name')
            saverecord.cust_address= request.POST.get('cust_address')
            saverecord.cust_phno = request.POST.get('cust_phno')
            saverecord.cust_email = request.POST.get('cust_email')
            saverecord.save()

            print('record saved succesfully!')
            messages.success(request,"Customer " + saverecord.cust_name + ' Added Successfully!')
            return render(request,'addcustomer.html')
        else:
            messages.success(request,'Failed!!! Please Enter Data Properly!')
            return render(request,'addcustomer.html')
    else:
        return render(request, 'addcustomer.html')


def managecustomers(request):
    showall = Customers.objects.all()
    return render(request,'managecustomers.html',{"customerdata":showall})

def EditCustomer(request,id):
    editcustomerobj= Customers.objects.get(id = id)
    return render(request,'editcustomer.html', {"Customer":editcustomerobj})

def UpdateCustomer(request,id):
   UpdateCustomer = Customers.objects.get(id = id) 
   form=Updatecustomerforms(request.POST, instance=UpdateCustomer)
   if form.is_valid():
       form.save()
       messages.success(request,'Record Updated Successfully!')
       return render(request, 'editcustomer.html',{"Customer":UpdateCustomer})

def DelCustomer(request,id):
    delcustomerobj = Customers.objects.get(id = id)
    delcustomerobj.delete()
    showdata = Customers.objects.all()
    return render(request,'managecustomers.html',{"customerdata":showdata})    