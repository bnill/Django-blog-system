# Generated by Django 2.1 on 2018-08-21 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantlocation',
            name='slug',
        ),
    ]
