from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Car
from .serializer import CarSerializer

# List all cars or create new one
class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterer_fields = ['make', 'year', 'price']
    permission_classes = [permissions.BasePermission]

# Retrieve, update, delete a car
class CarRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

