# Libreria para manejar colas de prioridad en Dijkstra, pero sin reemplazar la logica del algoritmo
import heapq

# Todo lo relacionado con el grafo, incluyendo la implementación del algoritmo de Dijkstra y la reconstrucción del camino más corto.
class grafo:

    # Inicializa un grafo vacío
    def __init__(self):
        self.vertices = {}

    # Crea los vértices y sus aristas con pesos
    def add_edge(self, origen, destino, peso):
        if origen not in self.vertices:
            self.vertices[origen] = []
        if destino not in self.vertices:
            self.vertices[destino] = []

        self.vertices[origen].append((destino, peso))
        self.vertices[destino].append((origen, peso))
    
    # Lógica del algoritmo para encontrar la ruta más corta
    def dijkstra(self, origen):
        distancias = {v: float('inf') for v in self.vertices}
        distancias[origen] = 0
        anterior = {v: None for v in self.vertices}
        visitados = set()

        cola = [(0, origen)]

        while cola:
            dist_actual, actual = heapq.heappop(cola)

            if actual in visitados:
                continue
            visitados.add(actual)

            for vecino, peso in self.vertices[actual]:
                nueva_dist = dist_actual + peso
                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    anterior[vecino] = actual
                    heapq.heappush(cola, (nueva_dist, vecino))
        return distancias, anterior

# Arma la lista de estaciones especificas que forman el camino más corto
def reconstruir_camino(anterior, origen, destino):
    camino = [destino]
    actual = destino

    while actual != origen:
        actual = anterior[actual]
        if actual is None:
            return None
        camino.append(actual)

    camino.reverse()
    return camino