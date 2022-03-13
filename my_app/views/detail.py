from xml.dom.minidom import CharacterData
from django.shortcuts import render
from django.views.generic import DetailView
from ..models import CharactorData

# Create your views here.
class CharactorDetail(DetailView):
    template_name = "detail.html"
    model = CharactorData