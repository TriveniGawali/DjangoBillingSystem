from django.urls import path
from . import views

urlpatterns = [

    path('generateinvoice/',views.generateinvoice,name = 'generateinvoice'),
    path('generateinvoice/invoiceprint/',views.invoiceprint,name = 'invoiceprint'),
]