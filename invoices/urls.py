from django.urls import path
from . import views

urlpatterns = [

    path('generateinvoice/',views.generateinvoice,name = 'generateinvoice'),
    path('generateinvoice/printinvoice/<int:id>',views.printinvoice,name = 'invoiceprint'),
    

    path('manageinvoices/',views.manageinvoices,name = 'manageinvoices'),
    path('delinvoice/<int:id>',views.DelInvoice,name='delinvoice'),

    path('generateinvoice/billsaved/',views.billsaved,name="billsaved"),
    path('generateinvoice/addorderproducts/',views.savebillproducts,name="addorderproducts"),
  
]