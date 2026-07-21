from grafo import grafo, reconstruir_camino

g = grafo()

g.add_edge("Portal", "Calle26", 4)
g.add_edge("Portal", "Museo", 1)
g.add_edge("Museo", "Calle26", 2)
g.add_edge("Calle26", "Centro", 1)
g.add_edge("Museo", "Centro", 5)
g.add_edge("Centro", "Universidad", 3)
g.add_edge("Calle26", "Universidad", 7)
g.add_edge("Universidad", "Parque", 2)

origen = "Portal"
destino = "Parque"

distancias, anterior = g.dijkstra(origen)
camino = reconstruir_camino(anterior, origen, destino)

print(f"Distancia más corta de {origen} a {destino}: {distancias[destino]}")
print(f"Camino: {' -> '.join(camino)}")