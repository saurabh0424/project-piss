# Generated by Django 2.0.7 on 2018-12-30 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('professors', '0010_auto_20181228_0608'),
    ]

    operations = [
        migrations.CreateModel(
            name='DislikedReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='LikedReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='dislike_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='like_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='likedreview',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professors.Review'),
        ),
        migrations.AddField(
            model_name='likedreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dislikedreview',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professors.Review'),
        ),
        migrations.AddField(
            model_name='dislikedreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
