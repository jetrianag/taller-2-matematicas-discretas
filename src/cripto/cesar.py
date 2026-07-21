alfabeto = 26
def desplazar_caracter(caracter: str, k: int) -> str:
    if caracter.isalpha():
        base = ord('A') if caracter.isupper() else ord('a')
        posicion = ord(caracter) - base 
        nueva_posicion = (posicion + k) % alfabeto
        return chr(base + nueva_posicion)  
    return caracter

    def cifrar_cesar(texto: str, k: int) -> str:
        k = k % alfabeto
        return ''.join(desplazar_caracter(c, k) for c in texto)

    def descifrar_cesar(texto: str, k: int) -> str:
        return cifrar_cesar(texto, -k)
    
    def fuerza_bruta_cesar(texto: str) -> dict:
        return {k: descifrar_cesar(texto, k) for k in range(alfabeto)}