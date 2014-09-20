from django.test import TestCase
from elearning.models import Anggota, Kursus, Materi, MateriIsi
from django.utils import timezone

class AnggotaTestCase(TestCase):
    def setUp(self):
        Anggota.objects.create(username="anggara", password="123456", nama="anggara jauhari", email="jauhari.anggara@gmail.com")
        Anggota.objects.create(username="harti", password="098765", nama="harti dwi hartiani", email="harti.dwi@gmail.com")
        Anggota.objects.create(username="khalifah", password="098765", nama="khalifah nazwa khalillah", email="khalifah.nazwa@gmail.com")

    def test_daftar_normal(self):
        anggotaBaru = Anggota()
        anggotaBaru.username ="umarfatih"
        anggotaBaru.password="102938"
        anggotaBaru.nama ="muhammad umar fatih"
        anggotaBaru.email="fatih.umar@gmail.com"
        anggotaBaru.daftar()

        anggotaHasil = Anggota.objects.get(pk=anggotaBaru.pk)
        self.assertEqual(anggotaHasil.nama,anggotaBaru.nama)

    def test_daftar_no_username(self):
        anggotaNoUsername = Anggota()
        anggotaNoUsername.password="102938"
        anggotaNoUsername.nama ="No username user"
        anggotaNoUsername.email="NoUsernameUser.umar@gmail.com"
        anggotaNoUsername.daftar()

        anggotaHasil = Anggota.objects.get(pk=anggotaNoUsername.pk)
        self.assertEqual(anggotaHasil,anggotaNoUsername)

    def test_get_anggota(self):
        anggara = Anggota.objects.get(id=1)
        self.assertEqual(anggara.username,"anggara")
