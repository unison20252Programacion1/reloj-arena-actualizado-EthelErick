def reloj_arena(m: int, s: str) -> str:
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    
    if m == 1:
        print(s)
        return
    
    # Para altura impar
    if m % 2 == 1:
        # Parte superior (decreciente)
        for i in range(m // 2 + 1):
            espacios = i
            caracteres = m - 2 * i
            print(" " * espacios + s * caracteres)
        
        # Parte inferior (creciente, sin repetir la línea del centro)
        for i in range(m // 2 - 1, -1, -1):
            espacios = i
            caracteres = m - 2 * i
            print(" " * espacios + s * caracteres)
    
    # Para altura par  
    else:
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
