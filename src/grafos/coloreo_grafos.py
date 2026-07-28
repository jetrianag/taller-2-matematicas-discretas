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
def resumen_por_color(colores: dict) -> dict:
    resumen = {}
    for vertice, color in colores.items():
        resumen.setdefault(color, []).append(vertice)
    return resumen
GRAFO_EJEMPLO = {
    "Calculo1":    ["Fisica1", "Algebra"],
    "Fisica1":     ["Calculo1", "Quimica"],
    "Algebra":     ["Calculo1", "ProgBasica", "Discretas"],
    "Quimica":     ["Fisica1", "Biologia"],
    "ProgBasica":  ["Algebra", "Discretas", "EstructurasDatos"],
    "Discretas":   ["Algebra", "ProgBasica", "EstructurasDatos"],
    "Biologia":    ["Quimica", "Estadistica"],
    "EstructurasDatos": ["ProgBasica", "Discretas", "BasesDatos"],
    "Estadistica": ["Biologia", "BasesDatos"],
    "BasesDatos":  ["EstructurasDatos", "Estadistica"],
}
def _menu():
    while True:
        print("\n--- Coloreo de grafos ---")
        print("1. Colorear el grafo de ejemplo (10 cursos)")
        print("2. Salir")
        opcion = input("Elige una opción (1-2): ").strip()
 
        if opcion == "1":
            colores = colorear_grafo_voraz(GRAFO_EJEMPLO)
            valido = es_coloreo_valido(GRAFO_EJEMPLO, colores)
            resumen = resumen_por_color(colores)
 
            print(f"\n¿Coloreo válido? {valido}")
            print(f"Colores usados: {len(resumen)}")
            for color, vertices in sorted(resumen.items()):
                print(f"  Color {color}: {vertices}")
 
        elif opcion == "2":
            print("Hasta luego.")
            break
 
        else:
            print("Opción no válida, intenta de nuevo.")
 
 
if __name__ == "__main__":
    _menu()
 