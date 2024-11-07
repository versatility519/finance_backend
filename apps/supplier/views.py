from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import (
    Supplier,
    SupplierItem,
    SupplierContact,
)
from .serializers import SupplierSerializer, SupplierItemSerializer, SupplierContactSerializer

class SupplierListCreateView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierItemListCreateView(generics.ListCreateAPIView):
    queryset = SupplierItem.objects.all()
    serializer_class = SupplierItemSerializer
    
class SupplierItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupplierItem.objects.all()
    serializer_class = SupplierItemSerializer

class SupplierContactListCreateView(generics.ListCreateAPIView):
    queryset = SupplierContact.objects.all()
    serializer_class = SupplierContactSerializer

class SupplierContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupplierContact.objects.all()
    serializer_class = SupplierContactSerializer
