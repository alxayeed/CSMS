# Generated by Django 2.2.4 on 2019-11-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20191106_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='PENDING', max_length=20),
            preserve_default=False,
        ),
    ]