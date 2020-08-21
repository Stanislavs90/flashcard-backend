from django.shortcuts import render
from rest_framework import viewsets
from cards.models import flash_card
from .serializers import flash_cardSerializer

class flash_cardViewSet(viewsets.ModelViewSet):
    """Viewset provides list, create, retrieve, update ,destroy"""
    queryset = flash_card.objects.all()
    serializer_class = flash_cardSerializer