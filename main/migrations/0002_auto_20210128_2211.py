# Generated by Django 3.1.3 on 2021-01-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='todo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='is_closed',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='is_favorite',
        ),
    ]
