from django.urls import path
from . import views

urlpatterns = [

    path('addcustomer/',views.addcustomer,name = 'addcustomer'),
    path('managecustomers/', views.managecustomers, name='managecustomers'),
    path('editcustomer/<int:id>',views.EditCustomer,name='editcustomer'),
    path('updatecustomer/<int:id>',views.UpdateCustomer,name='updatecustomer'),
    path('delcustomer/<int:id>',views.DelCustomer,name='delcustomer'),
]