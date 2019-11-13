# Generated by Django 2.2.4 on 2019-11-13 16:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Employe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employe',
            name='contact_no',
            field=models.PositiveSmallIntegerField(default=21324),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employe',
            name='date_joined',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employe',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employe',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employe',
            name='password',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employe',
            name='work_area',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Employe.Area'),
            preserve_default=False,
        ),
    ]
