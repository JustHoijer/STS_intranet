# Generated by Django 4.2.6 on 2023-11-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('display_board', '0004_rename_title_slide_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to='slides'),
        ),
    ]
