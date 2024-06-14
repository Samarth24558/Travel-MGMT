from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="home"),
    path('insert/', views.insert,name='insert'),
    path('insert_list/', views.insert_list,name='insert_list'),
    path('party_gc/', views.party_gc,name='party_gc'),
    path('all_gc_list/', views.all_gc_list,name='all_gc_list'),
    path('consignor_insert/', views.consignor_insert,name='consignor_insert'),
    path('consignor_list/', views.consignor_list,name='consignor_list'),
    path('consignee_insert/', views.consignee_insert,name='consignee_insert'),
    path('consignee_list/', views.consignee_list,name='consignee_list'),
]

