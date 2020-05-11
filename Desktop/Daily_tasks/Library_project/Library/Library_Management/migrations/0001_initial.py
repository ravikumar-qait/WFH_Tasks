# Generated by Django 2.2.11 on 2020-05-08 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='books',
            fields=[
                ('ISBN', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('available', models.BooleanField(default=True)),
                ('quantity', models.IntegerField(default=10)),
                ('author', models.ForeignKey(default='-', on_delete=django.db.models.deletion.SET_DEFAULT, to='Library_Management.authors')),
                ('genre', models.ForeignKey(default='-', on_delete=django.db.models.deletion.SET_DEFAULT, to='Library_Management.genre')),
                ('issued_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]