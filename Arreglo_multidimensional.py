def bubble_sort(matriz):
    """
    Función que implementa el algoritmo Bubble Sort para ordenar una matriz bidimensional.

    Args:
    - matriz: La matriz bidimensional que se desea ordenar.

    Returns:
    - La matriz ordenada.
    """
    # Convertir la matriz a una lista de listas para facilitar el ordenamiento
    lista = [elemento for fila in matriz for elemento in fila]

    # Aplicar Bubble Sort
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    # Convertir la lista ordenada nuevamente a una matriz bidimensional
    matriz_ordenada = [lista[i:i + len(matriz[0])] for i in range(0, len(lista), len(matriz[0]))]

    return matriz_ordenada


# Matriz
matriz = [
    [9, 5, 3],
    [2, 7, 1],
    [6, 4, 8]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la matriz utilizando Bubble Sort
matriz_ordenada = bubble_sort(matriz)

# Mostrar la matriz ordenada
print("\nMatriz ordenada:")
for fila in matriz_ordenada:
    print(fila)




