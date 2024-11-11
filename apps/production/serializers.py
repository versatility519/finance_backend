from rest_framework import serializers
from .models import Production, ProductionItem, Pdocument

from apps.project.models import Project
from apps.project.serializers import ProjectSerializer

from apps.inventory.models import OrderUnit
from apps.inventory.serializers import OrderUnitSerializer

class PdocumentSerializer(serializers.ModelSerializer):
    production = serializers.PrimaryKeyRelatedField(queryset=Production.objects.all())
    class Meta:
        model = Pdocument
        fields = ['id', 'doc_name', 'docs', 'production']

class ProductionItemSerializer(serializers.ModelSerializer):
    measure_unit = serializers.PrimaryKeyRelatedField(queryset=OrderUnit.objects.all())
    class Meta:
        model = ProductionItem
        fields = [
            'id', 'name', 'description', 'quantity', 'manufacturer', 'manufacturer_code', 'measure_unit', 'approved', 'approved_quantity', 'status', 'production'
            ]
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['measure_unit'] = OrderUnitSerializer(instance.measure_unit).data
        return representation
    
class ProductionSerializer(serializers.ModelSerializer):
    items = ProductionItemSerializer(many=True, required=False)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    
    class Meta:
        model = Production
        fields = [
            'id', 'name', 'project', 'date', 'p_start_date', 'p_end_date', 'p_status', 'approved', 'approved_by', 'items'
        ]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)        
        representation['project'] = ProjectSerializer(instance.project).data
        representation['items'] = ProductionItemSerializer(instance.items.all(), many=True).data
        
        return representation

        
