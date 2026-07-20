class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, origen, destino, peso):
        if origen not in self.vertices:
            self.vertices[origen] = []
        if destino not in self.vertices:
            self.vertices[destino] = []

        self.vertices[origen].append((destino, peso))
        self.vertices[destino].append((origen, peso))