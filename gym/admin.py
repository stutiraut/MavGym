from django.contrib import admin

from .models import Staff, Customer, Activity, Equipment

# Register your models here.
# Staff model
@admin.register(Staff)
class StaffList(admin.ModelAdmin):
    list_display = ('staff_name', 'staff_email', 'staff_phone')
    list_filter = ('staff_name',)
    search_fields = ('staff_name',)
    ordering = ['staff_name']

# customer model
@admin.register(Customer)
class CustomerList(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'customer_phone')
    list_filter = ('customer_name',)
    search_fields = ('customer_name',)
    ordering = ['customer_name']


# Activity model
@admin.register(Activity)
class ActivityList(admin.ModelAdmin):
    list_display = ('activity_name', 'activity_location', 'time')
    list_filter = ('activity_name',)
    search_fields = ('activity_name',)
    ordering = ['activity_name']

# Activity model
@admin.register(Equipment)
class EquipmentList(admin.ModelAdmin):
    list_display = ('customer_name', 'equipment_name','equipment_description')
    list_filter = ('customer_name', 'equipment_name')
    search_fields = ('customer_name','equipment_name')
    ordering = ['customer_name','equipment_name']
