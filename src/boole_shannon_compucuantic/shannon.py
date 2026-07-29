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


