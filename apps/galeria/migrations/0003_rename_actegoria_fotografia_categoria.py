# Generated by Django 5.0.6 on 2024-05-26 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_actegoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='actegoria',
            new_name='categoria',
        ),
    ]
