from rest_framework import serializers
from datetime import timedelta
from .models import Supplier, Contact, Invoice, InvoiceItem, Document, TaxInfo, Terms

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'address']

class ContactSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer() 

    class Meta:
        model = Contact
        fields = ['id', 'Fname', 'Lname', 'email', 'phone', 'address', 'role', 'supplier']
    
    def create(self, validated_data):
        supplier_data = validated_data.pop('supplier')
        supplier = Supplier.objects.create(**supplier_data)
        contact = Contact.objects.create(supplier=supplier, **validated_data)
        return contact
    
    def update(self, instance, validated_data):
        supplier_data = validated_data.pop('supplier', None)

        if supplier_data:
            for attr, value in supplier_data.items():
                setattr(instance.supplier, attr, value)
            instance.supplier.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
   
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'name', 'docs']

class TaxInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxInfo
        fields = ['id', 'name', 'rate', 'description']

class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = ['id', 'name']

class InvoiceItemSerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = InvoiceItem
        fields = ['id', 'name', 'description', 'unit', 'quantity', 'price', 'total_amount', 'tax_group']

    def get_total_amount(self, obj):
        return obj.price * obj.quantity
    
class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer()
    supplier = SupplierSerializer()
    docs = DocumentSerializer(read_only=True, required=False)
    terms = TermsSerializer()  # Keep this as is for input
    tax = TaxInfoSerializer()
 
    class Meta:
        model = Invoice
        fields = ['id', 'invoice_num', 'date_created', 'supplier', 'items', 'required_date', 
                  'status', 'ship_to', 'bill_to', 'docs', 'terms', 'tax']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        terms_data = validated_data.pop('terms', None)

        if terms_data:
            terms_instance = Terms.objects.create(**terms_data)
            validated_data['terms'] = terms_instance

        invoice = super().create(validated_data)

        for item_data in items_data:
            InvoiceItem.objects.create(invoice=invoice, **item_data)

        self.calculate_required_date(invoice)

        return invoice

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