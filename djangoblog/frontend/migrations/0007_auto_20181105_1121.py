# Generated by Django 2.0.6 on 2018-11-05 05:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_auto_20181101_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdata',
            name='data',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogdata',
            name='posted_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 5, 11, 21, 9, 580180)),
        ),
        migrations.AlterField(
            model_name='blogdata',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 5, 11, 21, 9, 580180)),
        ),
    ]
