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