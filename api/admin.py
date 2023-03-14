from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass


@admin.register(CropFamily)
class CropFamilyAdmin(admin.ModelAdmin):
    pass


@admin.register(CropType)
class CropTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(CompanionPlant)
class CompanionPlantAdmin(admin.ModelAdmin):
    pass


@admin.register(PrecedingCrop)
class PrecedingCropAdmin(admin.ModelAdmin):
    pass

