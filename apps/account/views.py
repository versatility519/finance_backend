from django.shortcuts import render
from rest_framework import generics
from .models import LegerAcc
from .serializers import LegerAccSerializer

# Create your views here.
class LegerAccListCreateView(generics.ListCreateAPIView):
    queryset = LegerAcc.objects.all()
    serializer_class = LegerAccSerializer

class LegerAccDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LegerAcc.objects.all()
    serializer_class = LegerAccSerializer