# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anggota',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('nama', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kursus',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('tanggal_mulai', models.DateField(verbose_name='tanggal mulai')),
                ('tanggal_selesai', models.DateField(verbose_name='tanggal selesai')),
                ('keterangan', models.CharField(max_length=255)),
                ('status', models.IntegerField(default=0)),
                ('tutor', models.ForeignKey(to='elearning.Anggota')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Materi',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('id_kursus', models.ForeignKey(to='elearning.Kursus')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Materi_isi',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('id_materi', models.ForeignKey(to='elearning.Materi')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
