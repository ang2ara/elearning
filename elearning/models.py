from django.db import models

"""
    Model Anggota
"""
class Anggota(models.Model):
    username = models.CharField(max_length=255,blank=False, null=False, unique= True)
    password  = models.CharField(max_length=255,blank=False, null=False)
    nama = models.CharField(max_length=255,blank=False, null=False)
    email = models.CharField(max_length=255,blank=False, null=False)

    def __str__(self):
        return self.username
    def daftar(self):
        return self.save()

"""
    Model KursusRelAnggota
"""
class KursusRelAnggota(models.Model):
    anggota = models.ForeignKey(Anggota)
    kursus = models.ForeignKey(Kursus)
    posisi = models.CharField(max_length=255,blank=False, null=False)

"""
    Model Kursus
"""
class Kursus(models.Model):
    nama = models.CharField(max_length=255)
    tanggal_mulai = models.DateField('tanggal mulai')
    tanggal_selesai = models.DateField('tanggal selesai')
    keterangan = models.CharField(max_length=255)
    tutor = models.ForeignKey(Anggota)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.nama

"""
    Model Materi
"""
class Materi(models.Model):
    nama = models.CharField(max_length=255)
    id_kursus = models.ForeignKey(Kursus)

    def __str__(self):
        return self.nama

"""
    Model MateriIsi
"""
class MateriIsi(models.Model):
    judul = models.CharField(max_length=255)
    id_materi = models.ForeignKey(Materi)

    def __str__(self):
        return self.judul

