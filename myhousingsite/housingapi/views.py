from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ResidentSerializer, ComplexSerializer, UnitSerializer, LeaseSerializer
from .models import Resident, Complex, Unit, Lease

# Create your views here.

class ResidentView(viewsets.ModelViewSet):
    serializer_class = ResidentSerializer
    queryset = Resident.objects.all()

class ComplexView(viewsets.ModelViewSet):
    serializer_class = ComplexSerializer
    queryset = Complex.objects.all()

class UnitView(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

class LeaseView(viewsets.ModelViewSet):
    serializer_class = LeaseSerializer
    queryset = Lease.objects.all()

# class GetCapacityView()