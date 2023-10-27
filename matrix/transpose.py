
def transpose(matrix):

    filas = len(matrix)
    columnas = len(matrix[0])

    matriz_transpuesta = []
    for _ in range(columnas):
        fila = [0] * filas
        matriz_transpuesta.append(fila)

    for i in range(filas):
        for j in range(columnas):
            matriz_transpuesta[j][i] = matrix[i][j]

    return matriz_transpuesta