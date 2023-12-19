# 1. profile company
# 2. company tersebut memiliki banyak gudang.
# 3. company tersebut juga memiliki banyak barang.
# 4.setiap gudang memiliki berbagai banyak jenis barang.
# 5.company mempunyai banyak karyawan setiap karyawan memiliki id yang berbeda.
# 6.database mencatat untuk mengetahui id karyawan yang membawa masuk atau keluar barang yang ada di gudang.
# 7.mencatat kapan barang yang ada di gudang masuk dan kapan barang di gudang keluar.
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

class Company(models.Model):
    name = models.CharField(max_length=100)

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    employee_id = models.AutoField(primary_key=True)

class Stock(models.Model):
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

class InventoryRecord(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    entry_type = models.CharField(max_length=50, choices=[('in', 'IN'), ('out', 'OUT')])
    entry_date = models.DateTimeField(auto_now_add=True)