from rest_framework import serializers
from .models import Registration
from django.conf import settings
User = settings.AUTH_USER_MODEL


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'ref_code','phone_number', 'mobile_network']
        read_only_fields = ['ref_code',  'created_at', 'updated_at']
    


