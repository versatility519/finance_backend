from rest_framework import generics
from .models import Supplier, Contact, Invoice, InvoiceItem, Document, TaxInfo, Terms
from .serializers import (
    SupplierSerializer,
    ContactSerializer,
    InvoiceSerializer,
    InvoiceItemSerializer,
    DocumentSerializer,
    TaxInfoSerializer,
    TermsSerializer,
)

# Supplier Views
class SupplierListCreateView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# Contact Views
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

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

# Document Views
class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

# Tax Item Views
class TaxInfoListCreateView(generics.ListCreateAPIView):
    queryset = TaxInfo.objects.all()
    serializer_class = TaxInfoSerializer

class TaxInfoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaxInfo.objects.all()
    serializer_class = TaxInfoSerializer

# Terms Views
class TermsListCreateView(generics.ListCreateAPIView):
    queryset = Terms.objects.all()
    serializer_class = TermsSerializer

class TermsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Terms.objects.all()
    serializer_class = TermsSerializer
