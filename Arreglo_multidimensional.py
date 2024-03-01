def bubble_sort_fila(matriz, fila):
    """
    Función que implementa el algoritmo Bubble Sort para ordenar una fila específica de una matriz bidimensional.

    Args:
    - matriz: La matriz bidimensional en la que se desea ordenar la fila.
    - fila: El índice de la fila que se desea ordenar.

    Returns:
    - La matriz con la fila especificada ordenada en orden ascendente.
    """
    # Aplicar Bubble Sort a la fila especificada
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]
    return matriz

# Matriz de ejemplo
matriz = [
    [9, 5, 3],
    [2, 7, 1],
    [6, 4, 8]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Índice de la fila que se desea ordenar (por ejemplo, la primera fila tiene índice 0)
fila_a_ordenar = 0

# Ordenar la fila especificada utilizando Bubble Sort
matriz_con_fila_ordenada = bubble_sort_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_con_fila_ordenada:
    print(fila)
