from django.contrib import admin
from elearning.models import Anggota, Kursus, Materi, MateriIsi, Kuis, KuisPertanyaan, KuisJawaban

""" Memasukkan Model Anggota kedalam halaman admin """
admin.site.register(Anggota)

""" Memasukkan Model Kursus kedalam halaman admin """
admin.site.register(Kursus)

""" Memasukkan Model Materi kedalam halaman admin """
admin.site.register(Materi)

""" Memasukkan Model MateriIsi kedalam halaman admin """
admin.site.register(MateriIsi)

""" Memasukkan Model Kuis kedalam halaman admin """
admin.site.register(Kuis)

""" Memasukkan Model KuisPertanyaan kedalam halaman admin """
admin.site.register(KuisPertanyaan)

""" Memasukkan Model KuisJawaban kedalam halaman admin """
admin.site.register(KuisJawaban)
