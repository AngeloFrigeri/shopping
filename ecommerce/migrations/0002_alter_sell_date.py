# Generated by Django 3.2 on 2021-04-08 13:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 8, 13, 54, 11, 968385), verbose_name='Data'),
        ),
    ]
