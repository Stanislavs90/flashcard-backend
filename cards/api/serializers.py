from ..models import flash_card
from rest_framework import serializers

class Flash_cardSerializer(serializers.ModelSerializer):
    class Meta:
        model = flash_card
        fields = ('question', 'answer')