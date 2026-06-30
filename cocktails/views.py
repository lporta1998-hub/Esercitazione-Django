from django.shortcuts import render
from django.views.generic import ListView
from cocktails.models import PuntoVendita
# Create your views here.


__all__ = [
    "PuntoVenditaListView",
]

class PuntoVenditaListView(ListView):
    model = PuntoVendita