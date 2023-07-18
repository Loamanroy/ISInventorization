from django.shortcuts import render
from rest_framework import generics

from .models import Catalog
from .serializers import CatalogSerializer


class CatalogAPIList(generics.ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
