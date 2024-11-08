from rest_framework import serializers
from .models import Journal, Transaction
from apps.account.models import LegerAccount

class LegerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegerAccount
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    # account = serializers.PrimaryKeyRelatedField(queryset=LegerAccount.objects.all()) 
    account = LegerAccountSerializer()
    class Meta:
        model = Transaction
        fields = ['id', 'name', 't_date', 'amount', 'description', 'type', 'account', 'journalID']

    def create(self, validated_data):
        account_data = validated_data.pop('account') 
        account, created = LegerAccount.objects.get_or_create(**account_data) 
        transaction = Transaction.objects.create(account=account, **validated_data) 
        return transaction
    
    def update(self, instance, validated_data):
        account_data = validated_data.pop('account', None) 
        if account_data:
            account, created = LegerAccount.objects.get_or_create(**account_data)  
            instance.account = account  

        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.description = validated_data.get('description', instance.description)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance
    
class JournalSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    total_debit = serializers.SerializerMethodField()
    total_credit = serializers.SerializerMethodField()
  
    class Meta:
        model = Journal
        fields = ['id', 'name', 'status', 's_date', 'e_date', 'number', 'transactions', 'total_debit', 'total_credit']

    def get_total_debit(self, obj):
        return sum(transaction.amount for transaction in obj.transactions.all() if transaction.type == 'debit')

    def get_total_credit(self, obj):
        return sum(transaction.amount for transaction in obj.transactions.all() if transaction.type == 'credit')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.number = validated_data.get('number', instance.number)
        instance.save()

        transactions_data = validated_data.pop('transactions', [])
        for transaction_data in transactions_data:
            transaction_id = transaction_data.get('id', None)
            if transaction_id:
                # Update existing transaction
                transaction = Transaction.objects.get(id=transaction_id)
                transaction.name = transaction_data.get('name', transaction.name)
                transaction.amount = transaction_data.get('amount', transaction.amount)
                transaction.description = transaction_data.get('description', transaction.description)
                transaction.type = transaction_data.get('type', transaction.type)
                transaction.save()
            else:
                # Create new transaction if no ID is provided
                Transaction.objects.create(journalID=instance, **transaction_data)
        return instance
    

    # def create(self, validated_data):
    #     transactions_data = validated_data.pop('transactions')
    #     journal = Journal.objects.create(**validated_data)
    #     for transaction_data in transactions_data:
    #         Transaction.objects.create(journalID=journal, **transaction_data)
    #     return journal
     