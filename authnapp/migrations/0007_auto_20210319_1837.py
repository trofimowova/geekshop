# Generated by Django 2.2.17 on 2021-03-19 18:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0006_auto_20210316_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 21, 18, 37, 24, 581844, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
