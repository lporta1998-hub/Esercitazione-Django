from django.urls import path
from cocktails.views import PuntoVenditaListView

urlpatterns = [
    path(
        'punto-vendita/',
        PuntoVenditaListView.as_view(),
        name="puntovendita_list"
    ),
]