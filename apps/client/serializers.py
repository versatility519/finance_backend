from rest_framework import serializers
from .models import Client,Contact

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'address', 'user', 'billing_address', 'shipping_address']

class ContactSerializer(serializers.ModelSerializer):
    clients = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'address', 'role', 'clients']


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['clients'] = instance.clients.name if instance.clients else None
        
        return representation