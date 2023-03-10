# Generated by Django 3.2.16 on 2022-12-15 17:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powers', '0003_alter_power_speed'),
    ]

    operations = [
        migrations.AddField(
            model_name='power',
            name='fire',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='power',
            name='flight',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='power',
            name='lasers',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='power',
            name='strength',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='power',
            name='total',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AddField(
            model_name='power',
            name='vision',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
