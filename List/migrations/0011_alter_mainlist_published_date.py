# Generated by Django 3.2.12 on 2022-03-31 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0010_listdetail_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainlist',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
    ]
