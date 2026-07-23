import random
 
MODULO_POR_DEFECTO = 1000003  # número sugerido en el enunciado
 
 
def generar_partes(nota: int, M: int = MODULO_POR_DEFECTO) -> tuple:
    s1 = random.randint(0, M - 1)
    s2 = random.randint(0, M - 1)
    s3 = (nota - s1 - s2) % M
    return s1, s2, s3