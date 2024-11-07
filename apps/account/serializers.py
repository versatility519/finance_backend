from rest_framework import serializers
from .models import LegerAcc, SubAccount

class SubAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubAccount
        fields = ['name', 'parent']
        
class LegerAccSerializer(serializers.ModelSerializer):
    sub_accounts = SubAccountSerializer(many=True, read_only=True)
    
    class Meta:
        model = LegerAcc
        fields = ['name', 'type', 'type_status', 'sub_accounts']
