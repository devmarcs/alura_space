# Generated by Django 5.0.1 on 2024-05-27 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_fotografia_pulicada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='pulicada',
            new_name='publicada',
        ),
    ]
