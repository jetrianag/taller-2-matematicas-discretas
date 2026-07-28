def colorear_grafo(grafo: dict) -> dict:
    colores = {}
    for vertice in grafo:
        colores_vecinos = {colores[vecino] for vecino in grafo[vertice] if vecino in colores}
        color = 0
        while color in colores_vecinos:
            color += 1
        colores[vertice] = color
    return colores
def es_coloreo_valido(grafo: dict, colores: dict) -> bool:
    for vertice, vecinos in grafo.items():
        for vecino in vecinos:
            if colores[vertice] == colores[vecino]:
                return False
    return True