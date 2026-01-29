import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.load_all_artists()
        self.nodi = []
        self.map = {}

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")

    def load_artists_with_min_albums(self, min_albums):
        pass

    def build_graph(self, n_alb):
        self.nodi = DAO.get_nodi(n_alb)
        self._graph.add_nodes_from(self.nodi)

        for nodo in self.nodi:
            self.map[nodo.id] = nodo

        self.archi = DAO.get_archi()
        for arco in self.archi:
            artista1 = self.map[arco[0]]
            artista2 = self.map[arco[1]]
            weight = arco[2]
            self._graph.add_edge(artista1, artista2, weight=weight)







