from rest_framework import serializers
from .models import flash_card


class flash_cardSerializer(serializers.ModelSerializer):
    class Meta:
        model = flash_card
        fields = "__all__"