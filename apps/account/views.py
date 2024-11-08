from django.shortcuts import render
from rest_framework import generics
from .models import LegerAccount, SubSAccount, SubAccount
from .serializers import LegerAccountSerializer, SubSAccountSerializer, SubAccountSerializer

# Create your views here.
class LegerAccountListCreateView(generics.ListCreateAPIView):
    queryset = LegerAccount.objects.all()
    serializer_class = LegerAccountSerializer

class LegerAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LegerAccount.objects.all()
    serializer_class = LegerAccountSerializer

class SubSAccountListCreateView(generics.ListCreateAPIView):
    queryset = SubSAccount.objects.all()
    serializer_class = SubSAccountSerializer
    
class SubSAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubSAccount.objects.all()
    serializer_class = SubSAccountSerializer

class SubAccountListCreateView(generics.ListCreateAPIView):
    queryset = SubAccount.objects.all()
    serializer_class = SubAccountSerializer
    
class SubAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubAccount.objects.all()
    serializer_class = SubAccountSerializer
    
