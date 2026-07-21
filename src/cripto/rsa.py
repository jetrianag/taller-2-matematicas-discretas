def euclides_extendido(a: int, b: int):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = euclides_extendido(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def inverso_modular(e: int, phi: int) -> int:
    g, x, _ = euclides_extendido(e, phi)
    if g != 1:
        raise ValueError(f"e={e} no es válido: mcd(e, phi(n))={g} (debe ser 1). "
            "Elige otro exponente e primo relativo con phi(n).")
    return x % phi

def generar_llaves(p: int, q: int, e: int) -> dict:
    n = p * q
    phi = (p - 1) * (q - 1)
    d = inverso_modular(e, phi)
    return {"p": p, "q": q, "n": n, "phi": phi, "e": e, "d": d}

def cifrar_rsa(mensaje: int, e: int, n: int) -> int:
    if mensaje >= n:
        raise ValueError(f"El mensaje M debe ser menor que n para que RSA funcione correctamente.")
    return pow(mensaje, e, n)

def descifrar_rsa(cifrado: int, d: int, n: int) -> int:
    return pow(cifrado, d, n)

def pedir_entero(mensaje: str) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

def _menu():
    llaves = None
 
    while True:
        print("\n--- RSA de juguete ---")
        if llaves:
            print(f"(Llaves activas: n={llaves['n']}, e={llaves['e']}, d={llaves['d']})")
        print("1. Generar llaves (p, q, e)")
        print("2. Cifrar un mensaje")
        print("3. Descifrar un mensaje")
        print("4. Salir")
        opcion = input("Elige una opción (1-4): ").strip()
 
        if opcion == "1":
            p = pedir_entero("Primo p: ")
            q = pedir_entero("Primo q: ")
            e = pedir_entero("Exponente público e: ")
            try:
                llaves = generar_llaves(p, q, e)
                print(f"n={llaves['n']}, phi(n)={llaves['phi']}, d={llaves['d']}")
            except ValueError as error:
                print(f"Error: {error}")
 
        elif opcion == "2":
            if not llaves:
                print("Primero genera las llaves (opción 1).")
                continue
            m = pedir_entero("Mensaje M a cifrar (entero menor que n): ")
            try:
                print(f"Cifrado C = {cifrar_rsa(m, llaves['e'], llaves['n'])}")
            except ValueError as error:
                print(f"Error: {error}")
 
        elif opcion == "3":
            if not llaves:
                print("Primero genera las llaves (opción 1).")
                continue
            c = pedir_entero("Cifrado C a descifrar: ")
            print(f"Mensaje descifrado M = {descifrar_rsa(c, llaves['d'], llaves['n'])}")
 
        elif opcion == "4":
            print("Hasta luego.")
            break
 
        else:
            print("Opción no válida, intenta de nuevo.")
 
 
if __name__ == "__main__":
    _menu()