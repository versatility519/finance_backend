from rest_framework import serializers
from datetime import timedelta
from .models import BillItem, BillDoc, Terms

from apps.inventory.models import OrderUnit
from apps.inventory.serializers import IssueUnitSerializer

from apps.account.models import LedgerAccount
from apps.account.serializers import LedgerAccountSerializer

from apps.organization.models import Tax
from apps.organization.serializers import TaxSerializer

from apps.client.models import Client, Contact
from apps.client.serializers import ClientSerializer, ContactSerializer

class BillDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDoc
        fields = ['id', 'name', 'docs']

class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = ['id', 'name']

class BillItemSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=LedgerAccount.objects.all())
    tax_group = serializers.PrimaryKeyRelatedField(queryset=Tax.objects.all())
    measure_unit = serializers.PrimaryKeyRelatedField(queryset=OrderUnit.objects.all())

    class Meta:
        model = BillItem
        fields = ['id', 'name', 'description', 'account', 'measure_unit', 'quantity', 'price', 'total', 'tax_amount', 'tax_group']

    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('total', None)
            self.fields.pop('tax_amount', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['measure_unit'] = IssueUnitSerializer(instance.measure_unit).data
        representation['account'] = LedgerAccountSerializer(instance.account).data
        representation['tax_group'] = TaxSerializer(instance.tax_group).data
        return representation

    # def get_total_amount(self, obj):
    #     # price = obj.price
    #     # quantity = Deciaml(obj.quantity)
    #     return obj.price * obj.quantity
    
    # def get_tax_amount(self, obj):
    #     return obj.price * obj.quantity * obj.tax_group.tax_rate
    
# class BillSerializer(serializers.ModelSerializer):
#     items = BillItemSerializer()
#     client = ClientSerializer()
#     docs = BillDocSerializer(read_only=True, required=False)
#     terms = TermsSerializer() 
#     tax = TaxSerializer()
 
#     class Meta:
#         model = Bill
#         fields = ['id', 'Bill_num', 'date_created', 'supplier', 'items', 'required_date', 
#                   'status', 'ship_to', 'bill_to', 'docs', 'terms', 'tax']

#     def create(self, validated_data):
#         items_data = validated_data.pop('items', [])
#         terms_data = validated_data.pop('terms', None)

#         # Bill= Bill.objects.create(**validated_data)
#         Bill = super().create(validated_data)

#         if terms_data:
#             terms_instance = Terms.objects.create(**terms_data)
#             validated_data['terms'] = terms_instance

#         for item_data in items_data:
#             BillItem.objects.create(Bill=Bill, **item_data)

#         self.calculate_required_date(Bill)

#         return Bill

#     def update(self, instance, validated_data):
#         terms_data = validated_data.pop('terms', None)
#         if terms_data:
#             terms_serializer = TermsSerializer(instance.terms, data=terms_data)
#             if terms_serializer.is_valid():
#                 terms_serializer.save()

#         # Update other fields
#         instance.Bill_num = validated_data.get('Bill_num', instance.Bill_num)
#         instance.date_created = validated_data.get('date_created', instance.date_created)
#         instance.required_date = validated_data.get('required_date', instance.required_date)
#         instance.status = validated_data.get('status', instance.status)
#         instance.ship_to = validated_data.get('ship_to', instance.ship_to)
#         instance.bill_to = validated_data.get('bill_to', instance.bill_to)
#         instance.save()

#         # Handle nested items
#         items_data = validated_data.get('items', [])
#         existing_items = {item.id: item for item in instance.items.all()} 

#         for item_data in items_data:
#             item_id = item_data.get('id', None)
#             if item_id and item_id in existing_items:
#                 # Update existing item
#                 item = existing_items[item_id]
#                 for attr, value in item_data.items():
#                     setattr(item, attr, value)
#                 item.save()
#             else:
#                 # Create new item
#                 BillItem.objects.create(Bill=instance, **item_data)

#         self.calculate_required_date(instance)

#         return instance

#     def calculate_required_date(self, Bill):
#         terms = Bill.terms.name if Bill.terms else None
#         if terms and terms.startswith("Net"):
#             try:
#                 # Extract the number of days from terms
#                 days = int(terms.split()[1])  # Split the string and get the second part
#                 # Calculate the required date
#                 Bill.required_date = Bill.date_created + timedelta(days=days)
#                 Bill.save()  # Save the updated Bill instance
#             except (IndexError, ValueError):
#                 # Handle invalid terms format or missing number of days
#                 pass