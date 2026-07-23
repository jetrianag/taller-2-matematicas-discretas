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

def simular_protocolo(notas: list, M: int = MODULO_POR_DEFECTO) -> dict:
    partes1, partes2, partes3 = repartir_notas(notas, M)
    suma1 = suma_parcial_servidor(partes1, M)
    suma2 = suma_parcial_servidor(partes2, M)
    suma3 = suma_parcial_servidor(partes3, M)
    suma_total = reconstruir_suma(suma1, suma2, suma3, M)
    promedio = calcular_promedio(suma_total, len(notas))
    return {
        "partes_servidor1": partes1,
        "partes_servidor2": partes2,
        "partes_servidor3": partes3,
        "suma_servidor1": suma1,
        "suma_servidor2": suma2,
        "suma_servidor3": suma3,
        "suma_total": suma_total,
        "promedio": promedio,
    }