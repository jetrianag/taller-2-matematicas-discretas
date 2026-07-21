#  Lo que se importa y desde dónde es para especificar que se estan importando la clase grafo y la función reconstruir_camino desde el archivo grafo.py que está en una carpeta distinta a la del archivo actual
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "grafos"))

from grafo import grafo, reconstruir_camino

def test_distancia_portal_a_parque():
    g = grafo()
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

    distancias, anterior = g.dijkstra("Portal")

    assert distancias["Parque"] == 25
    assert reconstruir_camino(anterior, "Portal", "Parque") == ["Portal", "Museo", "Estadio", "Centro", "Universidad", "Parque"]