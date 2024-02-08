from django.contrib import admin
from .models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','age','phone_no']


admin.site.register(Customer, CustomerAdmin)
