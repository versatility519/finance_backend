from rest_framework import generics
from .models import (
    Pdocument, Production, ProductionItem
)
from .serializers import (
    PdocumentSerializer, ProductionSerializer, ProductionItemSerializer
)

class PdocumentListCreateView(generics.ListCreateAPIView):
    queryset = Pdocument.objects.all()
    serializer_class = PdocumentSerializer

class ProductionListCreateView(generics.ListCreateAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer
    
class ProductionItemListCreateView(generics.ListCreateAPIView):
    queryset = ProductionItem.objects.all()
    serializer_class = ProductionItemSerializer
    
class ProductionItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductionItem.objects.all()
    serializer_class = ProductionItemSerializer
    
class ProductionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer

class PdocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pdocument.objects.all()
    serializer_class = PdocumentSerializer