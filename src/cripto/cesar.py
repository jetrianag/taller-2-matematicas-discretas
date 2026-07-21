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
    
    def menu_principal_programa():
        while True:
            print("=== Cifrado César ===")
            print("1. Cifrar texto")
            print("2. Descifrar texto")
            print("3. Fuerza bruta")
            print("4. Salir")
            opcion = input("Seleccione una opción (1-4): ").strip()

            if opcion == '1':
                texto = input("Ingrese el texto a cifrar: ")
                k = int(input("Ingrese el valor de desplazamiento (k): "))
                resultado = cifrar_cesar(texto, k)
                print(f"Texto cifrado: {resultado}")
            elif opcion == '2':
                texto = input("Ingrese el texto a descifrar: ")
                k = int(input("Ingrese el valor de desplazamiento (k): "))
                resultado = descifrar_cesar(texto, k)
                print(f"Texto descifrado: {resultado}")
            elif opcion == '3':
                texto = input("Texto cifrado (k desconocido): ")
                resultados = fuerza_bruta_cesar(texto)
                for k, descifrado in resultados.items():
                    print(f"k={k}: {descifrado}")
            elif opcion == '4':
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")