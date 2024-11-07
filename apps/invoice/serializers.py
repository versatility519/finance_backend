from rest_framework import serializers
from django.core.exceptions import  ValidationError
from datetime import timedelta
from .models import Invoice, InvoiceItem, InvoiceDoc, Terms

from apps.inventory.models import IssueUnit
from apps.inventory.serializers import IssueUnitSerializer

from apps.account.models import LegerAcc
from apps.account.serializers import LegerAccSerializer

from apps.organization.models import Tax
from apps.organization.serializers import TaxSerializer

from apps.client.models import Client, Contact
from apps.client.serializers import ClientSerializer, ContactSerializer

class InvoiceDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDoc
        fields = ['id', 'name', 'docs']

class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = ['id', 'name']

class InvoiceItemSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=LegerAcc.objects.all()) 
    tax_group = serializers.PrimaryKeyRelatedField(queryset=Tax.objects.all()) 
    measure_unit = serializers.PrimaryKeyRelatedField(queryset=IssueUnit.objects.all())
    
    class Meta:
        model = InvoiceItem
        fields = ['id', 'name', 'description', 'account', 'measure_unit', 'quantity', 'price', 'total', 'tax_amount', 'tax_group']
   
    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('total', None)
            self.fields.pop('tax_amount', None)

        if request and request.method == 'PUT':
            self.fields.pop('total', None)
            self.fields.pop('tax_amount', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['measure_unit'] = IssueUnitSerializer(instance.measure_unit).data
        representation['account'] = LegerAccSerializer(instance.account).data
        representation['tax_group'] = TaxSerializer(instance.tax_group).data
        return representation

class InvoiceSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())  
    # items = InvoiceItemSerializer(many=True)  # Assuming items can be multiple

    # total_tax_amount = serializers.SerializerMethodField()
    # total_net_amount = serializers.SerializerMethodField()
    # total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ['id', 'invoice_num', 'created_date', 'client', 'items', 'required_date', 
                  'status', 'ship_to', 'bill_to', 'docs', 'terms', 'total_tax_amount', 'total_net_amount', 'total_amount', 'contact']

    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('total_tax_amount', None)
            self.fields.pop('total_net_amount', None)
            self.fields.pop('total_amount', None)
        super().__init__(*args, **kwargs)
 
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['contact'] = ContactSerializer(instance.contact).data
        representation['client'] = ClientSerializer(instance.client).data
        return representation

    # def get_total_tax_amount(self, obj):
    #     print("Calculating total tax amount...")
    #     return sum(item.tax_amount for item in obj.items.all())
    
    # def get_total_net_amount(self, obj):
    #     return sum(item.total for item in obj.items.all())
    
    # def get_total_amount(self, obj):
    #     return self.get_total_net_amount(obj) + self.get_total_tax_amount(obj)

    # def calculate_required_date(self, invoice):
    #     terms = invoice.terms.name if invoice.terms else None
    #     if terms and terms.startswith("Net"):
    #         try:
    #             days = int(terms.split()[1])
    #             invoice.required_date = invoice.created_date + timedelta(days=days)
    #             invoice.save()
    #         except (IndexError, ValueError):
    #             pass