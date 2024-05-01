from django.contrib import admin
from .models import Driver, DriverProfile, Inspection, OrderAssignment, Vehicle

# Register your models here.
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display=Driver.DisplayFields
    list_filter=Driver.FilterFields 

@admin.register(DriverProfile)
class DriverProfileAdmin(admin.ModelAdmin):
    list_display=DriverProfile.DisplayFields
    list_filter=DriverProfile.FilterFields 

@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display=Inspection.DisplayFields
    list_filter=Inspection.FilterFields 

@admin.register(OrderAssignment)
class OrderAssignmentAdmin(admin.ModelAdmin):
    list_display=OrderAssignment.DisplayFields
    list_filter=OrderAssignment.FilterFields 

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display=Vehicle.DisplayFields
    list_filter=Vehicle.FilterFields 