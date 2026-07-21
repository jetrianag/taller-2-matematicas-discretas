# Importación de la clase grafo y la función reconstruir_camino desde el archivo grafo.py
from grafo import grafo, reconstruir_camino

# Se crea una instancia de la clase grafo
g = grafo()

# Se van creando los vertices y sus aristas junto a sus pesos para esa instancia g del clase grafo
g.add_edge("Portal", "Calle26", 12)
g.add_edge("Portal", "Museo", 5)
g.add_edge("Museo", "Calle26", 8)
g.add_edge("Calle26", "Centro", 6)
g.add_edge("Museo", "Centro", 15)
g.add_edge("Centro", "Universidad", 9)
g.add_edge("Calle26", "Universidad", 20)
g.add_edge("Universidad", "Parque", 7)
g.add_edge("Museo", "Estadio", 10)
g.add_edge("Estadio", "Centro", 4)
g.add_edge("Estadio", "Terminal", 11)
g.add_edge("Terminal", "Parque", 6)

# Se define un punto A y B arbitrarios como el inicio y el final de un camino a analizar
origen = "Museo"
destino = "Universidad"

# Se llama el método dijkstra para obtener la distancia mínima del camino
distancias, anterior = g.dijkstra(origen)
camino = reconstruir_camino(anterior, origen, destino)

# Se imprimen los resultados de la distancia más corta y el camino encontrado
print(f"Distancia más corta de {origen} a {destino}: {distancias[destino]}")
print(f"Camino: {' -> '.join(camino)}")