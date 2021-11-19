from django.urls import path
from . import views

urlpatterns = [
    path('addproduct/',views.addproduct,name = 'addproduct'),
    path('manageproducts/', views.manageproducts, name='manageproducts'),
    path('editproduct/<int:id>',views.EditProduct,name='editproduct'),
    path('updateproduct/<int:id>',views.UpdateProduct,name='updateproduct'),
    path('delproduct/<int:id>',views.DelProduct,name='delproduct'),
]
