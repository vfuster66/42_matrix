from ex00.matrix import Matrix


def transpose(matrix: Matrix) -> Matrix:
    """Retourne la transposée d'une matrice."""
    rows, cols = matrix.shape()

    transposed_values = []
    for j in range(cols):
        transposed_row = []
        for i in range(rows):
            transposed_row.append(matrix.values[i][j])
        transposed_values.append(transposed_row)

    return Matrix(transposed_values)
