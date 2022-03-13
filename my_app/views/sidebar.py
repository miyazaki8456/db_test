from django.shortcuts import render
from django.views.generic import TemplateView
from ..models import CharactorData

# Create your views here.
class Sidebar(TemplateView):
    template_name = "sidebar.html"
    model = CharactorData





