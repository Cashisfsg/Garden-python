# Generated by Django 4.1.5 on 2023-02-18 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CropFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CropType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('min_ph', models.DecimalField(blank=True, decimal_places=1, max_digits=3)),
                ('max_ph', models.DecimalField(blank=True, decimal_places=1, max_digits=3)),
                ('required_irrigation', models.IntegerField(blank=True, choices=[(1, 'очень мало'), (2, 'мало'), (3, 'умеренно'), (4, 'много'), (5, 'очень много')], null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='plants/')),
                ('crop_family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plant', to='api.cropfamily')),
                ('crop_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plant', to='api.croptype')),
            ],
        ),
        migrations.CreateModel(
            name='PrecedingCrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship_type', models.CharField(max_length=50)),
                ('crop_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.croptype')),
                ('plants', models.ManyToManyField(related_name='preceding_crops', to='api.plant')),
            ],
        ),
        migrations.CreateModel(
            name='CompanionPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.BooleanField(default=False)),
                ('plant1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companion_plant1', to='api.plant')),
                ('plant2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companion_plant2', to='api.plant')),
            ],
        ),
    ]
