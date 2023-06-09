# Generated by Django 3.2 on 2023-03-26 09:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_genre_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(regex='^[-a-zA-Z0-9_]+$')], verbose_name='URL'),
        ),
    ]
