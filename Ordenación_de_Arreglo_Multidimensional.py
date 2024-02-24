def bubble_sort(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    n = rows * cols

    for _ in range(n):
        for i in range(rows):
            for j in range(cols - 1):
                if matrix[i][j] > matrix[i][j + 1]:
                    matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]

    return matrix

#sxx matriz bidimensional
matrix = [
    [5, 2, 9],
    [10, 1, 4],
    [7, 6, 3]
]

print("Matriz original:")
for row in matrix:
    print(row)

sorted_matrix = bubble_sort(matrix)

print("\nMatriz ordenada:")
for row in sorted_matrix:
    print(row)
