from django.urls import path
from . import views

urlpatterns = [

    path('newpurchase/',views.newpurchase,name = 'newpurchase'),
    path('newpurchase/savepurchaseorder/',views.savepurchaseorder,name="savepurchaseorder"),
    path('managepurchase/',views.managepurchase ,name = 'managepurchase'),
    path('delpurchase/<int:id>',views.DelPurchase,name='delpurchase'),
    path('newpurchase/printpurchase/<int:id>',views.printpurchase,name = 'printpurchase'),

]