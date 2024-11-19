from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Carrier, Supplier, SupplierItem, SupplierContact, ShippingItem, ShipDocs, Shipping, SupplierPO
from .serializers import (
    CarrierSerializer, SupplierSerializer, SupplierItemSerializer,
    SupplierContactSerializer, ShippingItemSerializer, ShipDocsSerializer,
    ShippingSerializer, SupplierPOSerializer
)

class CarrierListCreateView(generics.ListCreateAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer

class CarrierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer

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

class ShippingItemCreateView(generics.CreateAPIView):
    queryset = ShippingItem.objects.all()
    serializer_class = ShippingItemSerializer

class ShippingItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShippingItem.objects.all()
    serializer_class = ShippingItemSerializer

class ShipDocsCreateView(generics.CreateAPIView):
    queryset = ShipDocs.objects.all()
    serializer_class = ShipDocsSerializer

class ShipDocsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShipDocs.objects.all()
    serializer_class = ShipDocsSerializer

class ShippingCreateView(generics.CreateAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

class ShippingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

class SupplierPOCreateView(generics.CreateAPIView):
    queryset = SupplierPO.objects.all()
    serializer_class = SupplierPOSerializer

class SupplierPODetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupplierPO.objects.all()
    serializer_class = SupplierPOSerializer
