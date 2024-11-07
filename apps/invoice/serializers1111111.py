from rest_framework import serializers
from datetime import timedelta
from .models import Invoice, InvoiceItem, InvoiceDoc, Terms

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
    
    class Meta:
        model = InvoiceItem
        fields = ['id', 'name', 'description', 'account', 'unit', 'quantity', 'price', 'total', 'tax_amount', 'tax_group']

    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('total', None)
            self.fields.pop('tax_amount', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['account'] = LegerAccSerializer(instance.account).data
        representation['tax_group'] = TaxSerializer(instance.tax_group).data
        return representation

class InvoiceSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())

    # terms = TermsSerializer(required=False)  # Allow terms to be nested
    # items = InvoiceItemSerializer()  # Allow multiple items
    # docs = InvoiceDocSerializer()

    # docs = serializers.PrimaryKeyRelatedField(queryset=InvoiceDoc.objects.all())
    # terms = serializers.PrimaryKeyRelatedField(queryset=Terms.objects.all())
    items = serializers.PrimaryKeyRelatedField(queryset=InvoiceItem.objects.all())
    
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

    
    def get_total_tax_amount(self, obj):
        return sum(item.total for item in obj.items.all())
    
    def get_total_net_amount(self, obj):
        return sum(item.total for item in obj.items.all())
    
    def get_total_amount(self, obj):
        return (obj.total_net_amount + obj.total_tax_amount)
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)

    #     # representation['items'] = InvoiceItemSerializer(instance.items.all(), many=True).data
    #     # representation['docs'] = InvoiceDocSerializer(instance.docs, many=True).data
    #     representation['client'] = ClientSerializer(instance.client).data
    #     representation['terms'] = TermsSerializer(instance.terms).data
    #     representation['contact'] = ContactSerializer(instance.contact).data
    #     return representation
  
    # def create(self, validated_data):
    #     items_data = validated_data.pop('items', [])
    #     terms_data = validated_data.pop('terms', None)

    #     # invoice= Invoice.objects.create(**validated_data)
    #     invoice = super().create(validated_data)

    #     if terms_data:
    #         terms_instance = Terms.objects.create(**terms_data)
    #         validated_data['terms'] = terms_instance

    #     for item_data in items_data:
    #         InvoiceItem.objects.create(invoice=invoice, **item_data)

    #     self.calculate_required_date(invoice)

    #     return invoice

    def update(self, instance, validated_data):
        terms_data = validated_data.pop('terms', None)
        if terms_data:
            terms_serializer = TermsSerializer(instance.terms, data=terms_data)
            if terms_serializer.is_valid():
                terms_serializer.save()

        # Update other fields
        instance.invoice_num = validated_data.get('invoice_num', instance.invoice_num)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.required_date = validated_data.get('required_date', instance.required_date)
        instance.status = validated_data.get('status', instance.status)
        instance.ship_to = validated_data.get('ship_to', instance.ship_to)
        instance.bill_to = validated_data.get('bill_to', instance.bill_to)
        instance.save()

        # Handle nested items
        items_data = validated_data.get('items', [])
        existing_items = {item.id: item for item in instance.items.all()} 

        for item_data in items_data:
            item_id = item_data.get('id', None)
            if item_id and item_id in existing_items:
                # Update existing item
                item = existing_items[item_id]
                for attr, value in item_data.items():
                    setattr(item, attr, value)
                item.save()
            else:
                # Create new item
                InvoiceItem.objects.create(invoice=instance, **item_data)

        self.calculate_required_date(instance)

        return instance
    
  

    def calculate_required_date(self, invoice):
        terms = invoice.terms.name if invoice.terms else None
        if terms and terms.startswith("Net"):
            try:
                # Extract the number of days from terms
                days = int(terms.split()[1])  # Split the string and get the second part
                # Calculate the required date
                invoice.required_date = invoice.date_created + timedelta(days=days)
                invoice.save()  # Save the updated invoice instance
            except (IndexError, ValueError):
                # Handle invalid terms format or missing number of days
                pass