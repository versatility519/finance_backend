from rest_framework import serializers
from apps.supplier.models import Supplier, SupplierItem, SupplierContact

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'supplier_name', 'address', 'billing_address', 'shipping_address','user']

class SupplierItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierItem
        fields = ['id', 'name', 'description', 'sku', 'measureUnit', 'manufacturer', 'manufacturer_code', 'quantity', 'growth', 'growth_fre','growth_per', 'tax_group']
        

class SupplierContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierContact
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'address', 'role', 'supplier']


 
