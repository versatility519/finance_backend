from rest_framework import serializers
from .models import Organization, Tax, Department
from apps.users.models import CustomUser

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']
        
class TaxSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())
    
    class Meta:
        model = Tax
        fields = ['id', 'tax_name', 'tax_rate', 'description', 'organization']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['organization'] = OrganizationSerializer(instance.organization).data
        return representation
        
class OrganizationSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
  
    class Meta:
        model = Organization
        fields = ('id', 'name', 'address', 'department', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
