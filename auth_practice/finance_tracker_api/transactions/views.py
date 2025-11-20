from django.shortcuts import render
from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from django.db.models import Sum

class TransactionViewSet(viewsets.ModelViewSet):
    "an unprotected viewset"
    # queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer
    permission_classes=[IsAuthenticated,IsOwner]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

