# Generated by Django 4.2.1 on 2023-05-23 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_menuitem_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='full_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='full_image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
