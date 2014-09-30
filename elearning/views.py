from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm

# import Model Kursus
from elearning.models import Kursus

# import Form Kursus
from elearning.forms import KursusForm

# view halaman index
class IndexView(generic.ListView):
    template_name= 'elearning/index.html'
    context_object_name = 'latest_kursus_list'

    def get_queryset(self):
        return Kursus.objects.order_by('nama')[:10]

# view halaman kursus
class KursusView(generic.DetailView):
    model = Kursus
    template_name = 'elearning/kursus.html'

# view halaman tambah kursus
class KursusTambahView(CreateView):
    model = Kursus
    template_name = 'elearning/kursus/tambah.html'
    form_class = KursusForm

    def get_initial(self):
        self.initial.update({ 'user': self.request.user })
        return self.initial

    def get_success_url(self):
        return reverse('index')
