from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import CreateAPIView, ListAPIView   

from .serializers import *
from .models import *

# Create your views here.
class PlantView(ListAPIView):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()


