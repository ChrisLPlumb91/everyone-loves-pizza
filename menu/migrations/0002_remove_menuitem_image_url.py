# Generated by Django 4.2.1 on 2023-05-20 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='image_url',
        ),
    ]
