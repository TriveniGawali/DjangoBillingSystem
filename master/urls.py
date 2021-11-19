from django.urls import path
from . import views

urlpatterns = [
    path('companyinfo/',views.Company_Info,name = 'companyinfo'),
]