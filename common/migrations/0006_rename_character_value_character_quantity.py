# Generated by Django 5.1 on 2024-08-29 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_rename_value_character_character_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='character_value',
            new_name='quantity',
        ),
    ]
