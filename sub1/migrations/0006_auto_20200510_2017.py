# Generated by Django 3.0.6 on 2020-05-10 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub1', '0005_auto_20200510_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='pictures_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 20, 17, 57, 787413), verbose_name='date published'),
        ),
    ]
