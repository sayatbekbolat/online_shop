from django.shortcuts import render

from rest_framework import viewsets
from .models import User, Product, Basket
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer
# Create your views here.
