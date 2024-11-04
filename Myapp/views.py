from django.shortcuts import render
from .models import Registration
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import RegisterSerializer
# Create your views here.
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegisterSerializer
   

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "User registered successfully. Please verify your account with the OTP sent."},
                        status=status.HTTP_201_CREATED)