# Generated by Django 4.2.1 on 2023-05-22 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_menuitem_calories_alter_menuitem_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='description',
            new_name='ingredients',
        ),
    ]