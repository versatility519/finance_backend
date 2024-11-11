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
        fields = ['id', 'doc_name', 'description', 'docfile', 'production']

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
    docs = PdocumentSerializer(many=True, required=False)

    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    
    class Meta:
        model = Production
        fields = [
            'id', 'name', 'project', 'date', 'p_start_date', 'p_end_date', 'p_status', 'approved', 'approved_by', 'items', 'docs'
        ]
    
    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('items', None)
            self.fields.pop('documents', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)        
        representation['project'] = ProjectSerializer(instance.project).data
        representation['items'] = ProductionItemSerializer(instance.items.all(), many=True).data
        representation['documents'] = PdocumentSerializer(instance.documents.all(), many=True).data
        
        return representation
