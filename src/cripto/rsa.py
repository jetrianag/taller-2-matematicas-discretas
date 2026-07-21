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