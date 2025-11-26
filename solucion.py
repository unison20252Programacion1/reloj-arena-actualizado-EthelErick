def reloj_arena(m: int, s: str) -> str:
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    
    if m == 1:
        print(s)
        return
    
    if m % 2 == 1:
        lineas_sup = m // 2
        ancho = m
    else:
        lineas_sup = m // 2 - 1
        ancho = m
    
    for i in range(lineas_sup + 1):
        espacios = i
        chars = ancho - 2 * i
        if chars > 0:
            print(" " * espacios + s * chars)
    
    for i in range(lineas_sup - 1, -1, -1):
        espacios = i
        chars = ancho - 2 * i
        if chars > 0:
            print(" " * espacios + s * chars)
        for i in range(m // 2 - 1, -1, -1):
            espacios = i
            caracteres = m - 2 * i
            print(" " * espacios + s * caracteres)
            print(" " * espacios + s * chars)
