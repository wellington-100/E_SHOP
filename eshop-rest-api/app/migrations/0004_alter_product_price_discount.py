# Generated by Django 5.0.1 on 2024-01-19 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_discount',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='price_dicount_reverse', to='app.money'),
        ),
    ]