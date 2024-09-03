# Generated by Django 5.1 on 2024-08-29 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_productvariant_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='product',
        ),
        migrations.AddField(
            model_name='maincharactertype',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_main_character_type', to='common.product'),
            preserve_default=False,
        ),
    ]
