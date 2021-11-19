from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from master.models import Company

# Create your views here.

def home(request):
    company = Company.objects.first()
    return render(request,'home.html',{"companydata":company})