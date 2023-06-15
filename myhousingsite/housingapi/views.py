from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
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

class UnitsByComplexView(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    http_method_names = ['get', ]
    
    def get_queryset(self):
        complex_id = self.request.GET.get('complex_id', None)
        self.queryset = Unit.objects.filter(complex=complex_id)
        return self.queryset
    
    # def get(self, request):
    #     units = Unit.objects.filter(complex=request.GET.get("complex_id"))
    #     serializer = UnitSerializer(units, many=True)
    #     print(request.GET)
    #     data = dict()
    #     return Response(serializer.data)
# class GetCapacityView()