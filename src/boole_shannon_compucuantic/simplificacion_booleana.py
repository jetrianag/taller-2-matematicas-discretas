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

