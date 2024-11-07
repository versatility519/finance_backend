from rest_framework import generics
from apps.organization.models import Tax
from .models import Invoice, InvoiceItem, InvoiceDoc, Terms
from .serializers import (
    InvoiceSerializer,
    InvoiceItemSerializer,
    InvoiceDocSerializer,
    TermsSerializer,
)
# InvoiceDoc Views
class InvoiceDocListCreateView(generics.ListCreateAPIView):
    queryset = InvoiceDoc.objects.all()
    serializer_class = InvoiceDocSerializer

class InvoiceDocDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceDoc.objects.all()
    serializer_class = InvoiceDocSerializer

# Terms Views
class TermsListCreateView(generics.ListCreateAPIView):
    queryset = Terms.objects.all()
    serializer_class = TermsSerializer

class TermsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Terms.objects.all()
    serializer_class = TermsSerializer

# Invoice Views
class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

# Invoice Views
class InvoiceItemListCreateView(generics.ListCreateAPIView):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer

class InvoiceItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer

