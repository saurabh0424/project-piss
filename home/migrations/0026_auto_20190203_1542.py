# Generated by Django 2.0.7 on 2019-02-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20190203_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivation',
            name='attempt_datetime',
            field=models.FloatField(default=1549188777.8302588),
        ),
    ]
