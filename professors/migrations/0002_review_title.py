# Generated by Django 2.0.7 on 2018-11-08 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default='-----', max_length=100),
        ),
    ]
