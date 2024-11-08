from rest_framework import serializers
from .models import LegerAccount, SubSAccount, SubAccount

# Serializer for SubAccount
class SubAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubAccount
        fields = ['id', 'name', 'parent'] 

# Serializer for SubSAccount
class SubSAccountSerializer(serializers.ModelSerializer):
    sub_account = SubAccountSerializer(many=True, read_only=True)
    
    class Meta:
        model = SubSAccount
        fields = ['id', 'name', 'parent', 'sub_account']

# Serializer for LegerAccount
class LegerAccountSerializer(serializers.ModelSerializer):
    subs_accounts = SubSAccountSerializer(many=True, read_only=True)
    
    class Meta:
        model = LegerAccount
        fields = ['id', 'LegerName', 'type', 'type_status', 'subs_accounts']
