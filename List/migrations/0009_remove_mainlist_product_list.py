# Generated by Django 3.2.12 on 2022-03-31 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0008_mainlist_product_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainlist',
            name='product_list',
        ),
    ]
