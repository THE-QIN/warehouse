from django.shortcuts import render
from .models import *

def company_profile(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'company_profile.html', context)

def warehouses(request):
    warehouses = Warehouse.objects.all()
    context = {'warehouses': warehouses}
    return render(request, 'warehouses.html', context)

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)

def employees(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employees.html', context)

def inventory_records(request):
    records = InventoryRecord.objects.all()
    context = {'records': records}
    return render(request, 'inventory_records.html', context)