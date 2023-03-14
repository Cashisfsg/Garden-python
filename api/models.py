from django.db import models


# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=50)
    crop_family = models.ForeignKey('CropFamily', related_name='plant', on_delete=models.CASCADE)
    crop_type = models.ForeignKey('CropType', related_name='plant', on_delete=models.CASCADE)
    min_ph = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    max_ph = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    required_irrigation = models.IntegerField(choices=((1, 'очень мало'),
                                                       (2, 'мало'),
                                                       (3, 'умеренно'),
                                                       (4, 'много'),
                                                       (5, 'очень много')), blank=True, null=True)
    img = models.ImageField(upload_to='plants/', null=True, blank=True)
    # companion_plant1
    # companion_plant2
    # preceding_crops

    def __str__(self):
        return self.name


class CropFamily(models.Model):
    name = models.CharField(max_length=50)
    # plant
    
    def __str__(self):
        return self.name


class CropType(models.Model):
    name = models.CharField(max_length=50)
    # plant

    def __str__(self):
        return self.name


class CompanionPlant(models.Model):
    plant1 = models.ForeignKey('Plant', on_delete=models.CASCADE, related_name='companion_plant1')
    plant2 = models.ForeignKey('Plant', on_delete=models.CASCADE, related_name='companion_plant2')
    relationship = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.plant1.name} - {self.plant2.name}: {self.relationship}"


class PrecedingCrop(models.Model):
    crop_type = models.ForeignKey('CropType', on_delete=models.CASCADE)
    relationship_type = models.CharField(max_length=50)
    plants = models.ManyToManyField('Plant', related_name='preceding_crops')

    def __str__(self):
        return self.plant.name