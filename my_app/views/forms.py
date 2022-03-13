from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from ..models import CharactorData

# Create your views here.
class Form(CreateView):
    template_name = "forms.html"
    model = CharactorData
    fields = ('name', 'force')

    success_url = reverse_lazy('list')