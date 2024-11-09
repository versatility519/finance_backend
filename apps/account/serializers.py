from rest_framework import serializers
from .models import LegerAccount, SubSAccount, SubOneAccount, SubTwoAccount, SubThreeAccount

# Serializer for SubThreeAccount
class SubThreeAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubThreeAccount
        fields = ['id', 'name', 'parent'] 

# Serializer for SubTwoAccount
class SubTwoAccountSerializer(serializers.ModelSerializer):
    two_layer_account = SubThreeAccountSerializer(many=True, read_only=True)
    
    class Meta:
        model = SubTwoAccount
        fields = ['id', 'name', 'parent', 'two_layer_account'] 

# Serializer for SubOneAccount
class SubOneAccountSerializer(serializers.ModelSerializer):
    one_layer_account = SubTwoAccountSerializer(many=True, read_only=True)
    class Meta:
        model = SubOneAccount
        fields = ['id', 'name', 'parent', 'one_layer_account'] 

# Serializer for SubSAccount
class SubSAccountSerializer(serializers.ModelSerializer):
    sub_account = SubOneAccountSerializer(many=True, read_only=True)
    
    class Meta:
        model = SubSAccount
        fields = ['id', 'name', 'parent', 'sub_account']

# Serializer for LegerAccount
class LegerAccountSerializer(serializers.ModelSerializer):
    subs_accounts = SubSAccountSerializer(many=True, read_only=True)
    
    class Meta:
        model = LegerAccount
        fields = ['id', 'LegerName', 'type', 'type_status', 'subs_accounts']
