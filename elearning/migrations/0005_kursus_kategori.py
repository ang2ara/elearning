# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0004_auto_20140925_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='kursus',
            name='kategori',
            field=models.ForeignKey(to='elearning.KategoriKursus', default=1),
            preserve_default=False,
        ),
    ]
