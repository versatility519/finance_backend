from django.shortcuts import render
from rest_framework import generics
from .models import LegerAcc, SubAccount
from .serializers import LegerAccSerializer, SubAccountSerializer

# Create your views here.
class LegerAccListCreateView(generics.ListCreateAPIView):
    queryset = LegerAcc.objects.all()
    serializer_class = LegerAccSerializer

class LegerAccDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LegerAcc.objects.all()
    serializer_class = LegerAccSerializer
    
class SubAccountListCreateView(generics.ListCreateAPIView):
    queryset = SubAccount.objects.all()
    serializer_class = SubAccountSerializer
    
class SubAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubAccount.objects.all()
    serializer_class = SubAccountSerializer
    
