from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.detail import DetailView

from elearning.models import Kursus

class IndexView(generic.ListView):
    template_name= 'elearning/index.html'
    context_object_name = 'latest_kursus_list'

    def get_queryset(self):
        return Kursus.objects.order_by('-tanggal_mulai')[:10]

class KursusView(generic.DetailView):
    model = Kursus
    template_name = 'elearning/kursus.html'
