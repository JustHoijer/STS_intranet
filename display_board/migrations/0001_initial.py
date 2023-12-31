# Generated by Django 4.2.6 on 2023-10-31 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('key', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('key', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('label', models.CharField(blank=True, max_length=120)),
                ('caption', models.CharField(blank=True, max_length=120)),
                ('image', models.ImageField(blank=True, upload_to='slides')),
                ('duration', models.IntegerField(blank=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slide',
                                             to='display_board.carousel')),
            ],
        ),
    ]
