# Se importan las librerías necesarias para la ejecución de los tests y para poder acceder a los archivos de la carpeta src/grafos desde la carpeta tests
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "grafos"))

from grafo import grafo
from cerrar_estacion import eliminar_vertice, comparar_impacto

# Prueba 1
def test_cierre_centro_impacto_variado():
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

    g_cerrado = eliminar_vertice(g, "Centro")

    pares = [
        ("Portal", "Parque"),
        ("Museo", "Universidad"),
        ("Portal", "Universidad"),
        ("Estadio", "Universidad"),
        ("Calle26", "Terminal")
    ]

    resultados = comparar_impacto(g, g_cerrado, pares)

    assert resultados[0]["estado"] == "SIN CAMBIO"
    assert resultados[1]["diferencia"] == 5
    assert resultados[2]["diferencia"] == 5
    assert resultados[3]["diferencia"] == 11
    assert resultados[4]["diferencia"] == 8

# Prueba 2
def test_cierre_portal_sin_impacto():
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

    g_cerrado = eliminar_vertice(g, "Portal")

    pares = [
        ("Museo", "Parque"),
        ("Calle26", "Terminal"),
        ("Museo", "Terminal"),
        ("Estadio", "Parque"),
        ("Centro", "Universidad")
    ]

    resultados = comparar_impacto(g, g_cerrado, pares)

    for r in resultados:
        assert r["estado"] == "SIN CAMBIO"

# Prueba 3
def test_cierre_provoca_desconexion():
    g = grafo()
    g.add_edge("A", "B", 2)
    g.add_edge("B", "C", 3)
    g.add_edge("C", "D", 4)
    g.add_edge("D", "E", 1)

    g_cerrado = eliminar_vertice(g, "C")

    pares = [("A", "E"), ("B", "D"), ("A", "B")]

    resultados = comparar_impacto(g, g_cerrado, pares)

    assert resultados[0]["estado"] == "DESCONECTADO"
    assert resultados[1]["estado"] == "DESCONECTADO"
    assert resultados[2]["estado"] == "SIN CAMBIO"