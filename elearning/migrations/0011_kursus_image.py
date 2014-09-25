# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0010_auto_20140926_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='kursus',
            name='image',
            field=models.ImageField(blank=True, verbose_name='thumb Pic', null=True, upload_to='images/cover/'),
            preserve_default=True,
        ),
    ]
