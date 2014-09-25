# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0003_auto_20140925_0326'),
    ]

    operations = [
        migrations.CreateModel(
            name='KategoriKursus',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nama', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='kursuskategori',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='anggotaakseskursus',
            name='anggota',
        ),
        migrations.RemoveField(
            model_name='kursus',
            name='kategori',
        ),
        migrations.DeleteModel(
            name='KursusKategori',
        ),
        migrations.RemoveField(
            model_name='kursus',
            name='tutor',
        ),
        migrations.RemoveField(
            model_name='kursusrelanggota',
            name='anggota',
        ),
        migrations.DeleteModel(
            name='Anggota',
        ),
    ]
