import random

def multiplicar_matriz_vector(matriz, vector):
    # multiplicacion normal de una matriz 2x2 por un vector de 2 entradas
    # (asi es como una compuerta cuantica transforma el estado del qubit)
    a, b = matriz[0]
    c, d = matriz[1]
    x, y = vector

    nuevo_x = a * x + b * y
    nuevo_y = c * x + d * y

    return [nuevo_x, nuevo_y]


def aplicar_compuerta(nombre_compuerta, estado):
    # arma la matriz de la compuerta pedida y la aplica al estado actual
    raiz2 = 2 ** 0.5

    if nombre_compuerta == "X":
        # X invierte el qubit: manda |0> a |1> y viceversa
        matriz = [[0, 1],
                  [1, 0]]
    elif nombre_compuerta == "Z":
        # Z deja |0> igual y le cambia el signo a |1>
        matriz = [[1, 0],
                  [0, -1]]
    elif nombre_compuerta == "H":
        # H pone el qubit en superposicion, mitad |0> mitad |1>
        matriz = [[1/raiz2, 1/raiz2],
                  [1/raiz2, -1/raiz2]]
    else:
        raise ValueError(f"Compuerta desconocida: {nombre_compuerta}")

    return multiplicar_matriz_vector(matriz, estado)