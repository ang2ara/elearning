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

    def __str_(self):
        return self.anggota.nama + " " + self.kursus.nama

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
    Model Anggota Akses Kursus
"""
class AnggotaAksesKursus(models.Model):
    anggota = models.ForeignKey(Anggota)
    kursus = models.ForeignKey(Kursus)
    tanggal_mulai = models.DateField("tanggal mulai")
    tanggal_selesai = models.DateField("tanggal selesai")

    def __str__(self):
        return anggota.nama + " " + kursus.nama

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

"""
    Model kuis
"""
class Kuis(models.Model):
    nama = models.CharField(max_length=255)
    tanggal_mulai = models.DateField("tanggal mulai")
    tanggal_selesai = models.DateField("tanggal selesai")
    kursus = models.ForeignKey(Kursus)

    def __str__(self):
        return self.nama
"""
    Model KuisPertanyaan
"""
class KuisPertanyaan(models.Model):
    pertanyaan = models.CharField(max_length=255)
    jenis = models.Model(max_length = 255)
    kuis = models.ForeignKey()

    def __str__(self):
        return self.pertanyaan


"""
    Model KuisJawaban
"""
class KuisJawaban(models.Model):
    jawaban  = models.CharField(max_length=255)
    pertanyaan = models.ForeignKey(KuisPertanyaan)

    def __str__(self):
        return self.jawaban
