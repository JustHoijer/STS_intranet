# Generated by Django 4.2.6 on 2023-11-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('display_board', '0005_alter_slide_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(blank=True, upload_to='slides'),
        ),
    ]
