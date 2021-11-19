from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Company
# Create your views here.
def Company_Info(request):
    comp1 = Company.objects.first()
    return render(request,'master.html',{'comp1':comp1})
    