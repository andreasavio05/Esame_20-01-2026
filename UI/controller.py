import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        num = self._view.txtNumAlbumMin.value
        try:
            num_int = int(num)
        except ValueError:
            self._view.show_alert("Inserisci un numero valido")
            return

        if num_int < 0:
            self._view.show_alert("Inserisci un numero valido")
            return

        self._model.build_graph(num_int)

        for nodo in self._model._graph.nodes:
            self._view.ddArtist.options.append(ft.dropdown.Option(nodo.name))

        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {len(self._model._graph.nodes)}. Numero di archi: {len(self._model._graph.edges)}"))
        self._view.update_page()

    def handle_connected_artists(self, e):
        pass

