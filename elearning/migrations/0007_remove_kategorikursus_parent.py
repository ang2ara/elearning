# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0006_kategorikursus_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategorikursus',
            name='parent',
        ),
    ]
