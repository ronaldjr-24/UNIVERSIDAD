# Define una matriz 3x3 con valores numéricos
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Define una función para buscar un valor en la matriz
def search_matrix(matrix, value):
    for row_index, row in enumerate(matrix):
        for col_index, element in enumerate(row):
            if element == value:
                return (row_index, col_index)
    return None

# Define el valor a buscar
value_to_find = 5

# Busca el valor en la matriz
result = search_matrix(matrix, value_to_find)

# Muestra el resultado
if result:
    print(f"Valor {value_to_find} encontrado en la posición {result} de la matriz.")
else:
    print(f"Valor {value_to_find} no encontrado en la matriz.")
