# Generated by Django 2.2.11 on 2020-05-12 08:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='deleted',
            name='deleted_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='list',
            name='created_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
