import os
import sys
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

path = os.path.abspath("db")
sys.path.append(path)

from apartmentsDAO import ApartmentsDAO
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

class UnitsByComplexView(APIView):

    def get(self, request):
        complex_id = self.request.GET.get('complex_id', None)
        lease_start = self.request.GET.get('lease_start', None)
        lease_end = self.request.GET.get('lease_end', None)
        apartmentsDAO = ApartmentsDAO('db/housing.db.sqlite3')
        response = apartmentsDAO.get_units_with_leases(complex_id, lease_start, lease_end)
        return Response(response)
    # serializer_class = UnitSerializer
    # http_method_names = ['get', ]
    
    # def get_queryset(self):
    #     complex_id = self.request.GET.get('complex_id', None)
    #     self.queryset = Unit.objects.filter(complex=complex_id)
    #     return self.queryset

class TestApiView(APIView):
    
    def get(self, request):
        complex_id = self.request.GET.get('complex_id', None)
        lease_start = self.request.GET.get('lease_start', None)
        lease_end = self.request.GET.get('lease_end', None)
        apartmentsDAO = ApartmentsDAO('db/housing.db.sqlite3')
        response = apartmentsDAO.get_units_with_leases(complex_id, lease_start, lease_end)
        return Response(response)

# class TestApiView(APIView):
    
#     def get(self, request):
#         apartmentsDAO = ApartmentsDAO('db/housing.db.sqlite3')
#         return Response(apartmentsDAO.get_units_with_leases())