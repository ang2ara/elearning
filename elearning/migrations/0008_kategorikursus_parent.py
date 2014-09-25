# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0007_remove_kategorikursus_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategorikursus',
            name='parent',
            field=models.ForeignKey(default=0, to='elearning.KategoriKursus', null=True, blank=True),
            preserve_default=True,
        ),
    ]
