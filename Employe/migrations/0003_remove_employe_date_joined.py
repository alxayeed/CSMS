# Generated by Django 2.2.4 on 2019-11-13 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employe', '0002_auto_20191113_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employe',
            name='date_joined',
        ),
    ]
