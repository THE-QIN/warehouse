from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("warehouse/", include("warehouse.urls")),
    path("admin/", admin.site.urls),
    path('warehouses/', views.warehouses, name='warehouses'),
    path('products/', views.products, name='products'),
    path('employees/', views.employees, name='employees'),
    path('inventory_records/', views.inventory_records, name='inventory_records'),
]