# Generated by Django 4.2.1 on 2023-05-22 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_rename_description_menuitem_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='description',
            field=models.TextField(blank=True, default=0, null=True),
        ),
    ]