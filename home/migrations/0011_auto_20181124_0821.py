# Generated by Django 2.0.7 on 2018-11-24 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20181124_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivation',
            name='attempt_datetime',
            field=models.FloatField(default=1543047683.1094086),
        ),
    ]
