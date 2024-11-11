from rest_framework import serializers
from .models import PurchaseOrder, PurchaseOrderItem, PurchaseDocument
from apps.inventory.models import OrderUnit
from apps.inventory.serializers import OrderUnitSerializer
from apps.organization.models import Tax, Department
from apps.organization.serializers import TaxSerializer, DepartmentSerializer
from apps.account.models import LedgerAccount
from apps.account.serializers import LedgerAccountSerializer
from apps.users.models import CustomUser
from apps.users.serializers import UserSerializer

class PurchaseDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDocument
        fields = ['id', 'doc_name', 'description', 'docfile', 'purchase_order']

class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    measure_unit = serializers.PrimaryKeyRelatedField(queryset=OrderUnit.objects.all())
    tax_group = serializers.PrimaryKeyRelatedField(queryset=Tax.objects.all())
    account = serializers.PrimaryKeyRelatedField(queryset=LedgerAccount.objects.all())
    purchaseOrder = serializers.PrimaryKeyRelatedField(queryset=PurchaseOrder.objects.all())

    class Meta:
        model = PurchaseOrderItem
        fields = ['id', 'name', 'description', 'manufacturer', 'manufacturer_code', 'measure_unit', 'quantity', 'price', 'net_amount', 'tax_amount', 'tax_group', 'account', 'purchaseOrder']
   
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['tax_group'] = TaxSerializer(instance.tax_group).data
        representation['account'] = LedgerAccountSerializer(instance.account).data
        representation['measure_unit'] = OrderUnitSerializer(instance.measure_unit).data
        return representation

    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('net_amount', None)
            self.fields.pop('tax_amount', None)
        super().__init__(*args, **kwargs)

class PurchaseOrderSerializer(serializers.ModelSerializer):
    items = PurchaseOrderItemSerializer(many=True)
    documents = PurchaseDocumentSerializer(many=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    
    class Meta:
        model = PurchaseOrder
        fields = ['id', 'name', 'description', 'date', 'ship_to', 'bill_to', 'department', 'created_by', 'approved', 'sent', 'items', 'documents']
    
    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('items', None)
            self.fields.pop('documents', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = PurchaseOrderItemSerializer(instance.items.all(), many=True).data
        representation['documents'] = PurchaseDocumentSerializer(instance.documents.all(), many=True).data
        
        representation['department'] = DepartmentSerializer(instance.department).data
        representation['created_by'] = UserSerializer(instance.created_by).data
        return representation
   