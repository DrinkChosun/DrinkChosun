# Generated by Django 3.2 on 2021-05-01 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alcohols', '0002_rename_alcohol_alcohols'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alcohols',
            new_name='Alcohol',
        ),
    ]