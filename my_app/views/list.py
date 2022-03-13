from xml.dom.minidom import CharacterData
from django.shortcuts import render
from django.views.generic import ListView
from ..models import CharactorData

# Create your views here.
class CharactorList(ListView):
    template_name = "list.html"
    model = CharactorData





