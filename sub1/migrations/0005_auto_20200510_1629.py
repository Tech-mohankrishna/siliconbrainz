# Generated by Django 3.0.6 on 2020-05-10 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub1', '0004_auto_20200510_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='pictures_thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='pictures_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 16, 29, 29, 684516), verbose_name='date published'),
        ),
    ]
