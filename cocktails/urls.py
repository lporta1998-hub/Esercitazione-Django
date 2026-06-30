from cocktails.views import PuntovenditaListView

urlpatterns = [
    path(
        'punto-vendita/',
        PuntovenditaListView.as_view(),
        name="puntovendita_list"
    ),
]