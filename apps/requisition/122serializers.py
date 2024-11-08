from rest_framework import serializers
from .models import Requisition, RequisitionItem, RequisitionDoc
from apps.organization.models import Tax, Department
from apps.organization.serializers import TaxSerializer, DepartmentSerializer

from apps.users.models import CustomUser
from apps.users.serializers import UserSerializer

from apps.supplier.models import Supplier
from apps.supplier.serializers import SupplierSerializer

from apps.inventory.models import OrderUnit
from apps.inventory.serializers import OrderUnitSerializer

class RequisitionDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisitionDoc
        fields = ['id', 'name', 'docs']

class RequisitionItemSerializer(serializers.ModelSerializer):
    tax_group = serializers.PrimaryKeyRelatedField(queryset=Tax.objects.all())
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    measureUnit = serializers.PrimaryKeyRelatedField(queryset=OrderUnit.objects.all())

    requisition = serializers.PrimaryKeyRelatedField(queryset=Requisition.objects.all())
    
    # requisition = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = RequisitionItem
        fields = ['id', 'name', 'description', 'measureUnit', 'manufacturer', 'manufacturer_code', 'supplier', 'quantity', 'price', 'total_amount', 'tax_amount', 'tax_group', 'reception_quantity', 'requisition']
        
    def __init__(self, instance=None, data=..., **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('total_amount', None)
            self.fields.pop('tax_amount', None)
        
        super().__init__(instance, data, **kwargs)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['tax_group'] = TaxSerializer(instance.tax_group).data
        # representation['measureUnit'] = OrderUnitSerializer(instance.measureUnit).data
        # representation['supplier'] = SupplierSerializer(instance.supplier).data
        # representation['requisition'] = RequisitionSerializer(instance.requisition).data   

        representation['supplier'] = instance.supplier.supplier_name if instance.supplier else None
        representation['measureUnit'] = instance.measureUnit.name if instance.measureUnit else None
        representation['tax_group'] = instance.tax_group.tax_rate if instance.tax_group else None
       
        # If you want to include the full requisition data, you can do this:
        return representation

class RequisitionSerializer(serializers.ModelSerializer):
    items = RequisitionItemSerializer(many=True)
    
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    approved_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    docs = serializers.PrimaryKeyRelatedField(queryset=RequisitionDoc.objects.all())

    class Meta:
        model = Requisition
        fields = ['id', 'requisition_number', 'date', 'docs', 'ship_to', 'bill_to', 'department', 'status', 'approved_by', 'created_by', 'total_net_amount', 'total_tax_amount', 'total_amount', 'items']

    # def create(self, validated_data):
    #     items_data = validated_data.pop('items')  # Extract items data
    #     requisition = Requisition.objects.create(**validated_data)  # Create Requisition instance
        
    #     # Create related items and set the requisition field
    #     for item_data in items_data:
    #         item_data['requisition'] = requisition  # Set the requisition field
    #         RequisitionItem.objects.create(**item_data)  # Create Item instance

    #     return requisition
    
    
    def save(self, **kwargs):
        instance = super().save(**kwargs)
        
        # Calculate totals from related items
        items = instance.items.all()
        instance.total_net_amount = sum(item.quantity * item.price for item in items)
        instance.total_tax_amount = sum(item.tax_amount for item in items)
        instance.total_amount = instance.total_net_amount + instance.total_tax_amount
        
        instance.save()
        return instance

    def __init__(self, instance=None, data=..., **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('items', None)
            self.fields.pop('total_net_amount', None)
            self.fields.pop('total_tax_amount', None)
            self.fields.pop('total_amount', None)
        
        super().__init__(instance, data, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = RequisitionItemSerializer(instance.items, many=True).data
        representation['department'] = DepartmentSerializer(instance.department).data
        representation['approved_by'] = UserSerializer(instance.approved_by).data
        representation['created_by'] = UserSerializer(instance.created_by).data
    
        representation['docs'] = RequisitionDocSerializer(instance.docs).data

        return representation

