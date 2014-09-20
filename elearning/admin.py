from django.contrib import admin
from elearning.models import Anggota, Kursus, Materi, MateriIsi

class AnggotaAdmin(admin.ModelAdmin):
    fieldsets=[
        (None, {'fields' : ["nama"]}),
    ]
    fieldsets = [
        (None,               {'fields' : ["question_text"]}),
        ("Date Information", {'fields' : ["pub_date"], 'classes': ['collapse']}),
    ]

admin.site.register(Anggota)
admin.site.register(Kursus)
admin.site.register(Materi)
admin.site.register(MateriIsi)
