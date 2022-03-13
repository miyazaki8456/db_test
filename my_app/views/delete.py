from django.shortcuts import render
from django.views.generic import DeleteView
from ..models import CharactorData
from django.urls import reverse_lazy

# Create your views here.
class Delete(DeleteView):
    template_name = "delete.html"
    model = CharactorData
    success_url = reverse_lazy('list')
