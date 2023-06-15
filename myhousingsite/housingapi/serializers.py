from rest_framework import serializers
from .models import Resident, Complex, Unit, Lease

class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ('resident_id', 'first_name', 'last_name', 'email', 'phone', 'birthdate', 'gender')

class ComplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complex
        fields = ('rowid', 'complex_name', 'street_address', 'type')

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('rowid', 'complex', 'unit_number', 'gender', 'room', 'bed', 'room_type', 'rent_price')

class LeaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lease
        fields = ('rowid', 'resident', 'unit', 'lease_start', 'lease_end', 'created_date')