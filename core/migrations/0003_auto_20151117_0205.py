# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('investment', models.ForeignKey(to='core.Investment')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='investment',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
