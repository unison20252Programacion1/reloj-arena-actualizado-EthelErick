# En este archivo debes implementar la función
#s caracter m lineas
def reloj_arena(m: int, s: str) -> str:
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    if m == 1:
        print(s)
        return
        #se cupone que ya esta corregida, por fin
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
