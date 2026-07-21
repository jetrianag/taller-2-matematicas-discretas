def euclides_extendido(a: int, b: int):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = euclides_extendido(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y