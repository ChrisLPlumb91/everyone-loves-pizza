# Generated by Django 4.2.1 on 2023-06-13 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_message_customermessage_user_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermessage',
            name='reason',
            field=models.IntegerField(choices=[('', 'Choose a reason'), (1, 'Giving feedback'), (2, 'Looking for information'), (3, 'Making a complaint'), (4, 'Other')], default=0),
        ),
    ]
