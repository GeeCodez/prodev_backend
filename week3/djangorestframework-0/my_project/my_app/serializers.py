from rest_framework import serializers
from .models import Book
from datetime import datetime
from django.utils.timezone import now

class BookSerializer(serializers.ModelSerializer):
    days_since_created=serializers.SerializerMethodField()
    class Meta:
        model=Book
        fields="__all__"
        
    def get_days_since_created(self,obj):
        delta=now()-obj.created_at
        return delta.days