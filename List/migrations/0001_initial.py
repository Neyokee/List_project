# Generated by Django 3.2.12 on 2022-03-31 11:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100, verbose_name='Название листа')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
