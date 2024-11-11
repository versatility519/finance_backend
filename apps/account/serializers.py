from rest_framework import serializers
from .models import LedgerAccount, SubAccount

class SubAccountSerializer(serializers.ModelSerializer):
    # This will ensure `children` is serialized as a list of sub-account dictionaries
    children = serializers.SerializerMethodField()

    class Meta:
        model = SubAccount
        fields = ['id', 'name', 'parent', 'children']

    def get_children(self, instance):
        # Query the related `children` objects and use the same serializer recursively
        children = instance.children.all()
        return SubAccountSerializer(children, many=True).data

    def create(self, validated_data):
        # Handles recursive creation of sub-accounts
        children_data = validated_data.pop('children', [])
        sub_account = SubAccount.objects.create(**validated_data)
        
        # Create each child recursively
        for child_data in children_data:
            child_data['parent'] = sub_account
            self.create(child_data)  # Recursive call for nested children
        
        return sub_account
    
class LedgerAccountSerializer(serializers.ModelSerializer):
    sub_accounts = SubAccountSerializer(many=True, required=False)

    class Meta:
        model = LedgerAccount
        fields = ['id', 'ledger_name', 'account_type', 'status_change', 'sub_accounts']

    def create(self, validated_data):
        sub_accounts_data = validated_data.pop('sub_accounts', [])
        ledger_account = LedgerAccount.objects.create(**validated_data)

        # Assign ledger_account to each sub-account recursively
        for sub_account_data in sub_accounts_data:
            sub_account_data['ledger_account'] = ledger_account
            SubAccountSerializer().create(sub_account_data)

        return ledger_account