from django.contrib import admin
from .models import Customers,Employees,Suppliers,Shippers,Categories,Products,Orders,OrderDetails

# Register your models here.
class Customers_Admin(admin.ModelAdmin):
        all_fields = [f.name for f in Customers._meta.fields]
        list_display=all_fields

class Employees_Admin(admin.ModelAdmin):
        all_fields = [f.name for f in Employees._meta.fields]
        list_display=all_fields

class Suppliers_Admin(admin.ModelAdmin):
        all_fields = [f.name for f in Suppliers._meta.fields]
        list_display=all_fields

class Shippers_Admin(admin.ModelAdmin):
        all_fields = [f.name for f in Shippers._meta.fields]
        list_display=all_fields

class Categories_Admin(admin.ModelAdmin):
        all_fields = [f.name for f in Categories._meta.fields]
        list_display=all_fields

class Products_Admin(admin.ModelAdmin):
        all_fields = [f.name for f in Products._meta.fields]
        list_display=all_fields

class Orders_Admin(admin.ModelAdmin):
        all_fields = [f.name for f in Orders._meta.fields]
        list_display=all_fields

class OrderDetails_Admin(admin.ModelAdmin):
        all_fields = [f.name for f in OrderDetails._meta.fields]
        list_display=all_fields

admin.site.register(Customers,Customers_Admin)
admin.site.register(Employees,Employees_Admin)
admin.site.register(Suppliers,Suppliers_Admin)
admin.site.register(Shippers,Shippers_Admin)
admin.site.register(Categories,Categories_Admin)
admin.site.register(Products,Products_Admin)
admin.site.register(Orders,Orders_Admin)
admin.site.register(OrderDetails,OrderDetails_Admin)
