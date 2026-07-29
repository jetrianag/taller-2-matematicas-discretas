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

