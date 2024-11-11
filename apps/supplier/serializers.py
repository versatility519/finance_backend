from rest_framework import serializers
from apps.supplier.models import Supplier, SupplierItem, SupplierContact

from apps.users.models import CustomUser
from apps.users.serializers import UserSerializer

from apps.inventory.models import OrderUnit
from apps.inventory.serializers import OrderUnitSerializer

from apps.account.models import LedgerAccount
from apps.account.serializers import LedgerAccountSerializer

from apps.organization.models import Tax
from apps.organization.serializers import TaxSerializer

class SupplierItemSerializer(serializers.ModelSerializer):
    measure_unit = serializers.PrimaryKeyRelatedField(queryset=OrderUnit.objects.all())
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    
    class Meta:
        model = SupplierItem
        fields = ['id', 'name', 'description', 'sku', 'measure_unit', 'manufacturer', 'manufacturer_code', 'quantity', 'growth', 'growth_fre', 'growth_per', 'supplier']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['measure_unit'] = OrderUnitSerializer(instance.measure_unit).data
 
        return representation
        

class SupplierContactSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    
    class Meta:
        model = SupplierContact
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'address', 'role', 'supplier']

class SupplierSerializer(serializers.ModelSerializer):
    supplier_items = SupplierItemSerializer(many=True, read_only=True)
    supplier_contact = SupplierContactSerializer(many=True, read_only=True)
    
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    account = serializers.PrimaryKeyRelatedField(queryset=LedgerAccount.objects.all())
    
    class Meta:
        model = Supplier
        fields = ['id', 'supplier_name', 'address', 'billing_address', 'shipping_address','user',  'account', 'supplier_items', 'supplier_contact']
        
    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('supplier_items', None)
            self.fields.pop('billDocs', None)
            self.fields.pop('total_tax_amount', None)
            self.fields.pop('total_net_amount', None)
            self.fields.pop('total_amount', None)
        super().__init__(*args, **kwargs)
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['account'] = LedgerAccountSerializer(instance.account).data
        
        representation['user'] = UserSerializer(instance.user).data
        
        representation['supplier_contact'] = SupplierContactSerializer(instance.supplier_contact.all(), many=True).data
        
        representation['supplier_items'] = SupplierItemSerializer(instance.supplier_items.all(), many=True).data
        
        return representation
    
        
 
