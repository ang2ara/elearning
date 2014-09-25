# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0002_auto_20140918_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnggotaAksesKursus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tanggal_mulai', models.DateField(verbose_name='tanggal mulai')),
                ('tanggal_selesai', models.DateField(verbose_name='tanggal selesai')),
                ('anggota', models.ForeignKey(to='elearning.Anggota')),
                ('kursus', models.ForeignKey(to='elearning.Kursus')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kuis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('tanggal_mulai', models.DateField(verbose_name='tanggal mulai')),
                ('tanggal_selesai', models.DateField(verbose_name='tanggal selesai')),
                ('kursus', models.ForeignKey(to='elearning.Kursus')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KuisJawaban',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('jawaban', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KuisPertanyaan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('pertanyaan', models.CharField(max_length=255)),
                ('jenis', models.CharField(max_length=255)),
                ('kuis', models.ForeignKey(to='elearning.Kuis')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KursusKategori',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(to='elearning.KursusKategori')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KursusRelAnggota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('posisi', models.CharField(max_length=255)),
                ('anggota', models.ForeignKey(to='elearning.Anggota')),
                ('kursus', models.ForeignKey(to='elearning.Kursus')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='kuisjawaban',
            name='pertanyaan',
            field=models.ForeignKey(to='elearning.KuisPertanyaan'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kursus',
            name='kategori',
            field=models.ForeignKey(to='elearning.KursusKategori', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anggota',
            name='username',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
