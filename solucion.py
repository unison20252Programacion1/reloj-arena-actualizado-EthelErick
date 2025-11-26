# En este archivo debes implementar la función
#s caracter m lineas
def reloj_arena(m: int, s: str) -> str:
    # Validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    
    # Implementar la lógica para generar el reloj de arena en ASCII
    n = m
    for j in range(m):
        espacios = (m - n) // 2
        print(" " * espacios + s * n)    
        if j < m // 2 - (1 if m % 2 == 0 else 0):
            n -= 2
        elif j >= m // 2:
            n += 2
        if n < 1:
            n = 1
if __name__ == "__main__":
    main()
        # Parte superior
        for i in range(m // 2):
            espacios = i
            caracteres = m - 2 * i
            print(" " * espacios + s * caracteres)
        
        # Parte inferior (simétrica)
        for i in range(m // 2 - 1, -1, -1):
            espacios = i
            caracteres = m - 2 * i
            print(" " * espacios + s * caracteres)
            print(" " * espacios + s * chars)
