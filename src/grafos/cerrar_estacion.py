# Importación de la clase grafo y la función reconstruir_camino desde el archivo grafo.py
from grafo import grafo, reconstruir_camino

# Se crea una copia del grafo original sin las conexiones que involucran el vértice a cerrar
def eliminar_vertice(g, vertice_a_cerrar):
    nuevo_grafo = grafo()

    # Este ciclo recorre los vertices del grafo original saltando aquel que se va a cerrar
    for v in g.vertices:
        # Si el vertice actual es el que se va a cerrar, se omite y no se agrega al nuevo grafo
        if v == vertice_a_cerrar:
            continue
        # Se recorren los vecinos del vertice actual. Si el vecino no es el vertice a cerrar, se agrega al nuevo grafo con su peso correspondiente
        for vecino, peso in g.vertices[v]:
            if vecino != vertice_a_cerrar:
                nuevo_grafo.add_edge(v, vecino, peso)

    return nuevo_grafo