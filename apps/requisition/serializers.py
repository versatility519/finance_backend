from rest_framework import serializers
from .models import Requisition, RequisitionItem, RequisitionDoc

from apps.organization.models import Department
from apps.organization.serializers import DepartmentSerializer

from apps.users.models import CustomUser
from apps.users.serializers import UserSerializer

from apps.supplier.models import Supplier
from apps.organization.models import Tax
from apps.inventory.models import OrderUnit

# Serializer for RequisitionDoc
class RequisitionDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisitionDoc
        fields = ['id', 'name', 'docs']

# Serializer for RequisitionItem
class RequisitionItemSerializer(serializers.ModelSerializer):
    measureUnit = serializers.PrimaryKeyRelatedField(queryset=OrderUnit.objects.all())
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), allow_null=True)
    tax_group = serializers.PrimaryKeyRelatedField(queryset=Tax.objects.all(), allow_null=True)
    
    class Meta:
        model = RequisitionItem
        fields = [
            'id', 'name', 'description', 'measureUnit', 'manufacturer', 'manufacturer_code', 
            'supplier', 'quantity', 'price', 'total_amount', 'tax_group', 'tax_amount', 
            'reception_quantity', 'requisition'
        ]
        read_only_fields = ['total_amount', 'tax_amount']  # Computed fields

    def save(self, **kwargs):
        # Override save to calculate tax_amount and total_amount before saving
        if self.validated_data.get('tax_group'):
            tax_rate = self.validated_data['tax_group'].tax_rate
            self.validated_data['tax_amount'] = self.validated_data['quantity'] * self.validated_data['price'] * tax_rate
        else:
            self.validated_data['tax_amount'] = 0
        
        self.validated_data['total_amount'] = self.validated_data['quantity'] * self.validated_data['price']
        return super().save(**kwargs)

# Serializer for Requisition
class RequisitionSerializer(serializers.ModelSerializer):
    items = RequisitionItemSerializer(many=True, read_only=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    approved_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    docs = serializers.PrimaryKeyRelatedField(queryset=RequisitionDoc.objects.all())

    class Meta:
        model = Requisition
        fields = [
            'id', 'requisition_number', 'date', 'docs', 'ship_to', 'bill_to', 'department', 
            'status', 'approved_by', 'created_by', 'total_net_amount', 'total_tax_amount', 
            'total_amount', 'items'
        ]
        read_only_fields = ['total_net_amount', 'total_tax_amount', 'total_amount']
    
    def __init__(self, instance=None, data=..., **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('items', None)
            # self.fields.pop('total_net_amount', None)
            # self.fields.pop('total_tax_amount', None)
            # self.fields.pop('total_amount', None)
        
        super().__init__(instance, data, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = RequisitionItemSerializer(instance.items, many=True).data
        representation['department'] = DepartmentSerializer(instance.department).data
        representation['approved_by'] = UserSerializer(instance.approved_by).data
        representation['created_by'] = UserSerializer(instance.created_by).data
    
        representation['docs'] = RequisitionDocSerializer(instance.docs).data

        return representation

    def create(self, validated_data):
        # Extract items data from validated_data or set to empty list if not provided
        items_data = validated_data.pop('items', [])
        
        # Step 1: Create the Requisition instance first
        requisition = Requisition.objects.create(**validated_data)
        
        # Initialize total calculations
        total_net = 0
        total_tax = 0

        # Step 2: Process each item data
        for item_data in items_data:
            item_data['requisition'] = requisition  # Link item to the requisition
            requisition_item = RequisitionItem.objects.create(**item_data)  # Save item

            # Accumulate totals
            total_net += requisition_item.total_amount
            total_tax += requisition_item.tax_amount

        # Step 3: Update the requisition totals
        requisition.total_net_amount = total_net
        requisition.total_tax_amount = total_tax
        requisition.total_amount = total_net + total_tax
        requisition.save()

        return requisition

    def to_representation(self, instance):
        # Customize the representation to show nested items and related fields
        representation = super().to_representation(instance)
        representation['items'] = RequisitionItemSerializer(instance.items, many=True).data
        representation['docs'] = RequisitionDocSerializer(instance.docs).data
        return representation