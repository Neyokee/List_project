# Generated by Django 3.2.12 on 2022-03-31 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0009_remove_mainlist_product_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='listdetail',
            name='ID',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='List.mainlist'),
        ),
    ]
