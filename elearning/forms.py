from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateInput, Select, FileInput
from elearning.models import Kursus
from django.utils.translation import ugettext_lazy as _

# form kursus
class KursusForm(forms.ModelForm):

    # inisialiasi form
    def __init__(self, *args, **kwargs):
        # membuat atribut user untuk menghubungkan obyek kursus dengan user
        self.user = kwargs['initial']['user']
        super(KursusForm, self).__init__(*args, **kwargs)

    # menyimpan obyek yang ada di dalam form kedalam database
    def save(self, commit=True):
        obj = super(KursusForm, self).save(False)
        obj.user = self.user
        commit and obj.save()
        return obj

    # konfigurasi field yang ada di form
    class Meta:
        model = Kursus
        fields = ['nama','keterangan','tanggal_mulai','tanggal_selesai','image','kategori']
        labels = {
            'image': _('Gambar Sampul'),
        }
        help_texts = {
            #'nama': _('Some useful help text.'),
        }
        error_messages = {
            'nama': {
                'max_length': _("Nama kursus terlalu panjang, maksimal 255 karakter."),
            },
            'keterangan': {
                'max_length': _("keterangan kursus terlalu panjang, maksimal 255 karakter."),
            },
        }
        widgets = {
            'nama': TextInput(attrs={'class': 'form-control'}),
            'keterangan': Textarea(attrs={'class': 'form-control'}),
            'tanggal_mulai': DateInput(attrs={'class': 'datepicker form-control'}),
            'tanggal_selesai': DateInput(attrs={'class': 'datepicker form-control'}),
            'image': FileInput(attrs={'class': 'form-control'}),
            'kategori': Select(attrs={'class': 'form-control'}),
        }

