from rest_framework import serializers
from .models import Sales, SalesItem
from apps.inventory.serializers import OrderSerializer, IssueSerializer
from apps.organization.serializers import DepartmentSerializer
from apps.account.serializers import LegerAccSerializer

class SalesItemSerializer(serializers.ModelSerializer):
    # messureUnit = OrderSerializer()
    account = LegerAccSerializer()
    class Meta:
        model = SalesItem
        fields = ['id', 'name', 'description', 'unit', 'quantity', 'price', 'manufacturer', 'manufacturer_code', 'tax_group', 'status', 'account']

class SalesSerializer(serializers.ModelSerializer):
    items = SalesItemSerializer(many=True)
    department = DepartmentSerializer()
    class Meta:
        model = Sales
        fields = ['id', 'created_date', 'ship_to', 'bill_to', 'items', 
                  'department', 'approved', 'approved_by', 'created_by', 'status']