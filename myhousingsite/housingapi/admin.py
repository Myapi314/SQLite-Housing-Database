from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Complex, Resident, Lease, Unit

class ResidentAdmin(admin.ModelAdmin):
    list_display = ('resident_id', 'first_name', 'last_name', 'email', 'phone', 'birthdate', 'gender')

class ComplexAdmin(admin.ModelAdmin):
    list_display = ('rowid', 'complex_name', 'street_address', 'type')

class LeaseAdmin(admin.ModelAdmin):
    list_display = ('rowid', 'resident', 'unit', 'lease_start', 'lease_end', 'created_date')

class UnitAdmin(admin.ModelAdmin):
    list_display = ('rowid', 'complex', 'unit_number', 'gender', 'room', 'bed', 'room_type', 'rent_price')

admin.site.register(Resident, ResidentAdmin)
admin.site.register(Complex, ComplexAdmin)
admin.site.register(Lease, LeaseAdmin)
admin.site.register(Unit, UnitAdmin)