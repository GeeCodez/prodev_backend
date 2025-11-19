from django.shortcuts import render
from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    "an unprotected viewset"
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer
