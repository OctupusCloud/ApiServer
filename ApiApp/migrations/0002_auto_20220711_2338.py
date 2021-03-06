# Generated by Django 3.2.7 on 2022-07-12 02:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interfaces',
            name='port',
            field=models.IntegerField(choices=[(0, 'Port 0'), (1, 'Port 1')], default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='interfaces',
            name='slot',
            field=models.IntegerField(choices=[(0, 'Slot 0'), (1, 'Slot 1')], default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)]),
        ),
    ]
