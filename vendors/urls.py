from django.urls import path
from . import views

urlpatterns = [

    path('addvendor/',views.addvendor,name = 'addvendor'),
    path('managevendors/', views.managevendors, name='managevendors'),
    path('editvendor/<int:id>',views.EditVendor,name='editvendor'),
    path('updatevendor/<int:id>',views.UpdateVendor,name='updatevendor'),
    path('delvendor/<int:id>',views.DelVendor,name='delvendor'),
]