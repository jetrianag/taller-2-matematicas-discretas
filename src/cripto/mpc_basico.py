import random
 
MODULO_POR_DEFECTO = 1000003  # número sugerido en el enunciado
 
 
def generar_partes(nota: int, M: int = MODULO_POR_DEFECTO) -> tuple:
    s1 = random.randint(0, M - 1)
    s2 = random.randint(0, M - 1)
    s3 = (nota - s1 - s2) % M
    return s1, s2, s3

def repartir_notas(notas: list, M: int = MODULO_POR_DEFECTO) -> tuple:
    partes_servidor1, partes_servidor2, partes_servidor3 = [], [], []
    for nota in notas:
        s1, s2, s3 = generar_partes(nota, M)
        partes_servidor1.append(s1)
        partes_servidor2.append(s2)
        partes_servidor3.append(s3)
    return partes_servidor1, partes_servidor2, partes_servidor3

def suma_parcial_servidor(partes_de_un_servidor: list, M: int = MODULO_POR_DEFECTO) -> int:
    return sum(partes_de_un_servidor) % M
def reconstruir_suma(suma1: int, suma2: int, suma3: int, M: int = MODULO_POR_DEFECTO) -> int:
    return (suma1 + suma2 + suma3) % M
def calcular_promedio(suma_total: int, cantidad_notas: int) -> float:
    if cantidad_notas == 0:
        raise ValueError("No hay notas para calcular el promedio.")
    return suma_total / cantidad_notas