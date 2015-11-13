# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lon', models.FloatField(null=True, verbose_name='Longitude', blank=True)),
                ('lat', models.FloatField(null=True, verbose_name='Latitude', blank=True)),
                ('label', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('filename', models.CharField(max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='coordinate',
            name='track_id',
            field=models.ForeignKey(to='map.Track'),
        ),
    ]
