# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0005_kursus_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategorikursus',
            name='parent',
            field=models.ForeignKey(null=True, default=1, to='elearning.KategoriKursus', blank=True),
            preserve_default=True,
        ),
    ]
