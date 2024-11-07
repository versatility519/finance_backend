
from rest_framework import serializers
from .models import Organization, Tax, Department

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'
        # fields = ['id', 'name', 'rate', 'description']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['organization'] = OrganizationSerializer(instance.organization).data
        return representation

class OrganizationSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    class Meta:
        model = Organization
        fields = ('id', 'name', 'address', 'department', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['department'] = DepartmentSerializer(instance.department).data
        return representation

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'