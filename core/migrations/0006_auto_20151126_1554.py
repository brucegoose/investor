# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151117_0440'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='visibility',
            field=models.IntegerField(default=0, choices=[(0, b'Public'), (1, b'Anonymous')]),
        ),
        migrations.AddField(
            model_name='investment',
            name='visibility',
            field=models.IntegerField(default=0, choices=[(0, b'Public'), (1, b'Anonymous')]),
        ),
    ]
