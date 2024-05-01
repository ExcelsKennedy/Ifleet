from django.contrib import admin
from .models import Order, CustomerProfile

# Register your models here.
@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    list_display=Order.DisplayFields
    list_filter=Order.FilterFields 

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display=CustomerProfile.DisplayFields
    list_filter=CustomerProfile.FilterFields 