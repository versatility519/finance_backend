from rest_framework import serializers
from django.core.exceptions import  ValidationError
from datetime import timedelta
from .models import Invoice, InvoiceItem, InvoiceDoc, Terms

from apps.inventory.models import IssueUnit
from apps.inventory.serializers import IssueUnitSerializer

from apps.account.models import LedgerAccount
from apps.account.serializers import LedgerAccountSerializer

from apps.organization.models import Tax
from apps.organization.serializers import TaxSerializer

from apps.client.models import Client, Contact
from apps.client.serializers import ClientSerializer, ContactSerializer

class InvoiceDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDoc
        fields = ['id', 'name', 'description', 'doc_file', 'invoice']

class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = ['id', 'name']

class InvoiceItemSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=LedgerAccount.objects.all()) 
    tax_group = serializers.PrimaryKeyRelatedField(queryset=Tax.objects.all()) 
    measure_unit = serializers.PrimaryKeyRelatedField(queryset=IssueUnit.objects.all())
    
    invoice = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all())
    
    class Meta:
        model = InvoiceItem
        fields = ['id', 'name', 'description', 'account', 'measure_unit', 'quantity', 'price', 'net_amount', 'tax_amount', 'tax_group', 'invoice']
   
    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('net_amount', None)
            self.fields.pop('tax_amount', None)

        if request and request.method == 'PUT':
            self.fields.pop('net_amount', None)
            self.fields.pop('tax_amount', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['measure_unit'] = IssueUnitSerializer(instance.measure_unit).data
        representation['account'] = LedgerAccountSerializer(instance.account).data
        representation['tax_group'] = TaxSerializer(instance.tax_group).data
        return representation

class InvoiceSerializer(serializers.ModelSerializer):
    items =  InvoiceItemSerializer(many=True)
    
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())  
    
    invoiceDocs = InvoiceDocSerializer(many=True)

    class Meta:
        model = Invoice
        fields = [
            'id', 'invoice_num', 'created_date', 'client', 'required_date', 
            'status', 'ship_to', 'bill_to', 'terms', 'total_tax_amount', 'total_net_amount', 'total_amount', 'contact', 'turn_to_pdf', 'items', 'invoiceDocs'
        ]

    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('items', None)
            self.fields.pop('invoiceDocs', None)
            self.fields.pop('total_tax_amount', None)
            self.fields.pop('total_net_amount', None)
            self.fields.pop('total_amount', None)
        super().__init__(*args, **kwargs)
 
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = InvoiceItemSerializer(instance.items.all(), many=True).data
        
        representation['invoiceDocs'] = InvoiceDocSerializer(instance.invoiceDocs.all(), many=True).data
        representation['terms'] = TermsSerializer(instance.terms).data
        representation['contact'] = ContactSerializer(instance.contact).data
        representation['client'] = ClientSerializer(instance.client).data
        return representation