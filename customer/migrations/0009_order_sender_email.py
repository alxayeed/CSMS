# Generated by Django 2.2.4 on 2019-11-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_order_reciever_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sender_email',
            field=models.EmailField(default='N/A', max_length=254),
            preserve_default=False,
        ),
    ]
