# Generated by Django 3.0.6 on 2020-05-10 06:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub1', '0002_auto_20200510_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='pictures_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 11, 43, 13, 701745), verbose_name='date published'),
        ),
    ]
