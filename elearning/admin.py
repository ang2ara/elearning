from django.contrib import admin
from elearning.models import Anggota, Kursus, Materi, MateriIsi

""" Memasukkan Model Anggota kedalam halaman admin """
admin.site.register(Anggota)

""" Memasukkan Model Kursus kedalam halaman admin """
admin.site.register(Kursus)

""" Memasukkan Model Materi kedalam halaman admin """
admin.site.register(Materi)

""" Memasukkan Model MateriIsi kedalam halaman admin """
admin.site.register(MateriIsi)
