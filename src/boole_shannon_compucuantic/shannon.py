import math

def frecuencia_texto(texto):
    # cuenta cuantas veces aparece cada simbolo (letra) en el texto
    frecuencia = {}

    for letra in texto:
        if letra in frecuencia:
            frecuencia[letra] += 1
        else:
            frecuencia[letra] = 1
    return frecuencia


def entropia_texto(frecuencia, texto):
    # entropia de Shannon: mide la incertidumbre del texto, no su longitud
    # un texto repetitivo tiene probabilidades muy concentradas en pocos
    # simbolos, entonces la entropia sale baja (o 0 si es un solo simbolo)
    suma = 0
    for letra in frecuencia:
        probabilidad = frecuencia[letra] / len(texto)
        suma -= probabilidad * math.log2(probabilidad)
    return suma

