from dataclasses import fields
from django.shortcuts import render
from django.views.generic import UpdateView
from ..models import CharactorData
from django.urls import reverse_lazy

# Create your views here.
class Update(UpdateView):
    template_name = "update.html"
    model = CharactorData
    fields = ('name', 'force')
    success_url = reverse_lazy('list')
