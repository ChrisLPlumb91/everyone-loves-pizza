# Generated by Django 4.2.1 on 2023-06-12 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customermessage',
            old_name='message',
            new_name='user_msg',
        ),
    ]
