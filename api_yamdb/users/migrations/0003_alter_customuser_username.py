# Generated by Django 3.2 on 2023-03-26 14:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230326_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.RegexValidator(message='Username must be Alphanumeric and not "me"', regex='^(?!me$)[\\w]+$'), django.core.validators.MinLengthValidator(5, message='Не менее 5 символов')], verbose_name='Имя пользователя'),
        ),
    ]