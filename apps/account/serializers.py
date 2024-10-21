from rest_framework import serializers
from .models import LegerAcc

class LegerAccSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LegerAcc
        fields = '__all__'
