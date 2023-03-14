from rest_framework.serializers import ModelSerializer, StringRelatedField

from .models import *

class PlantSerializer(ModelSerializer):
    family = StringRelatedField()

    class Meta:
        model = Plant
        fields = ("id", "name", "family", "img")

