# Generated by Django 5.0.6 on 2024-05-28 03:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_rename_pulicada_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='date_fotography',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
