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

# Recibe un grafo original, un grafo con un vértice cerrado y una lista de pares de vértices (origen, destino)
def comparar_impacto(g_original, g_cerrado, pares):
    # Se inicializa una lista vacía para almacenar los resultados de las comparaciones
    resultados = []

    for origen, destino in pares:
        # Distancia antes del cierre, usando el grafo original
        distancias_antes, _ = g_original.dijkstra(origen)
        distancia_antes = distancias_antes[destino]

        # Distancia despues del cierre, usando el grafo modificado
        distancias_despues, _ = g_cerrado.dijkstra(origen)
        distancia_despues = distancias_despues[destino]

        # Se determina el estado del camino después del cierre del vértice
        if distancia_despues == float('inf'):
            estado = "DESCONECTADO"
            diferencia = None
        elif distancia_despues > distancia_antes:
            estado = "MÁS LARGO"
            diferencia = distancia_despues - distancia_antes
        else:
            estado = "SIN CAMBIO"
            diferencia = 0

        # Se agregan los resultados de la comparación a la lista de resultados
        resultados.append({
            "origen": origen,
            "destino": destino,
            "antes": distancia_antes,
            "despues": distancia_despues if distancia_despues != float('inf') else "N/A",
            "diferencia": diferencia,
            "estado": estado
        })

    return resultados

# Se crea una instancia del grafo y se agregan los vértices y aristas con sus respectivos pesos
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

# Se define el vértice que se desea cerrar y se crea un nuevo grafo sin ese vértice
vertice_cerrado = "Centro"
g_cerrado = eliminar_vertice(g, vertice_cerrado)

# Se definen los pares de vértices (origen, destino) para los cuales se desea comparar las distancias antes y después del cierre del vértice
pares = [
    ("Portal", "Parque"),
    ("Museo", "Universidad"),
    ("Portal", "Universidad"),
    ("Estadio", "Universidad"),
    ("Calle26", "Terminal")
]

# Se llama a la función comparar_impacto para obtener los resultados de las comparaciones de distancias antes y después del cierre del vértice
resultados = comparar_impacto(g, g_cerrado, pares)

# Se imprimen los resultados de las comparaciones en un formato tabular, mostrando el origen, destino, distancia antes del cierre, distancia después del cierre, diferencia y estado del camino
print(f"Estación cerrada: {vertice_cerrado}\n")
print(f"{'Origen':<12}{'Destino':<12}{'Antes':<8}{'Después':<10}{'Diferencia':<12}{'Estado'}")
for r in resultados:
    print(f"{r['origen']:<12}{r['destino']:<12}{r['antes']:<8}{str(r['despues']):<10}{str(r['diferencia']):<12}{r['estado']}")