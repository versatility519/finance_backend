from rest_framework import serializers
from .models import Client,Contact

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'address', 'user', 'billing_address', 'shipping_address']

class ContactSerializer(serializers.ModelSerializer):
    clients = ClientSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'address', 'role', 'clients']

