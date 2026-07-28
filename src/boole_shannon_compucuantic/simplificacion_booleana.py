from itertools import product

def num_a_binario(n, num_vars):
    return format(n, f"0{num_vars}b") #Convierte un numero a su representacion de bits


def se_combinan(term1, term2):
    diferencias = 0
    resultado = []
    for b1, b2 in zip(term1, term2):
        if b1 != b2:
            diferencias += 1
            resultado.append("-")
        else:
            resultado.append(b1)
    if diferencias == 1:
        return "".join(resultado)
    return None


def encontrar_implicantes_primos(minterminos, num_vars):
    # grupo inicial: (termino_binario, {minterminos que representa})
    grupo_actual = {num_a_binario(m, num_vars): {m} for m in minterminos}

    implicantes_primos = {}  # termino -> set de minterminos que cubre
    while grupo_actual:
        combinados = {}
        usados = set()
        terminos = list(grupo_actual.keys())

        for i in range(len(terminos)):
            for j in range(i + 1, len(terminos)):
                nuevo = se_combinan(terminos[i], terminos[j])
                if nuevo is not None:
                    usados.add(terminos[i])
                    usados.add(terminos[j])
                    cubiertos = grupo_actual[terminos[i]] | grupo_actual[terminos[j]]
                    combinados[nuevo] = combinados.get(nuevo, set()) | cubiertos

        # los terminos que NO se combinaron con nadie son implicantes primos
        for termino in terminos:
            if termino not in usados:
                implicantes_primos[termino] = grupo_actual[termino]

        grupo_actual = combinados

    return implicantes_primos


def elegir_implicantes_esenciales(implicantes_primos, minterminos):
    """
    Construye una tabla de cobertura (que implicante cubre que minterminos)
    y selecciona un conjunto minimo de implicantes primos que cubra todos
    los minterminos:
      1) primero los ESENCIALES (el unico que cubre cierto minterm)
      2) luego, de forma golosa, los que cubren mas minterminos restantes
    """
    pendientes = set(minterminos)
    seleccionados = []

    # Paso 1: implicantes esenciales
    for m in list(pendientes):
        cubridores = [t for t, cubiertos in implicantes_primos.items() if m in cubiertos]
        if len(cubridores) == 1 and cubridores[0] not in seleccionados:
            seleccionados.append(cubridores[0])

    for t in seleccionados:
        pendientes -= implicantes_primos[t]

    # Paso 2: cobertura golosa de lo que falta
    while pendientes:
        mejor = max(
            implicantes_primos,
            key=lambda t: len(implicantes_primos[t] & pendientes)
        )
        if len(implicantes_primos[mejor] & pendientes) == 0:
            break
        if mejor not in seleccionados:
            seleccionados.append(mejor)
        pendientes -= implicantes_primos[mejor]

    return seleccionados


def termino_a_expresion(termino, nombres_variables):
    """
    Convierte un termino binario con '-' (p. ej. '1-0') en un producto
    (AND) de literales, p. ej. 'A AND (NOT B)'.
    Bit '1' -> variable en positivo. Bit '0' -> variable negada.
    Bit '-' -> variable no aparece (fue eliminada al simplificar).
    """
    literales = []
    for bit, var in zip(termino, nombres_variables):
        if bit == "1":
            literales.append(var)
        elif bit == "0":
            literales.append(f"NOT {var}")
    if not literales:
        return "1"  # la funcion es siempre verdadera
    return " AND ".join(literales)


def simplificar(minterminos, num_vars, nombres_variables=None):
    """
    Funcion principal: recibe los minterminos y devuelve
    (lista_de_terminos_elegidos, expresion_en_texto)
    """
    if nombres_variables is None:
        nombres_variables = ["A", "B", "C", "D"][:num_vars]

    if not minterminos:
        return [], "0"  # funcion siempre falsa

    implicantes_primos = encontrar_implicantes_primos(minterminos, num_vars)
    elegidos = elegir_implicantes_esenciales(implicantes_primos, minterminos)

    productos = [termino_a_expresion(t, nombres_variables) for t in elegidos]
    expresion = " OR ".join(f"({p})" for p in productos)
    return elegidos, expresion

