from ex00.matrix import Matrix
from ex00.vector import Vector


def matmul(a, b):
    """Multiplie une matrice par un vecteur ou une autre matrice."""

    # Cas Matrice * Vecteur
    if isinstance(a, Matrix) and isinstance(b, Vector):
        rows_a, cols_a = a.shape()
        if cols_a != b.size():
            raise ValueError("Matrix columns must match Vector size.")

        result_values = []
        for row in a.values:
            # Produit scalaire de la ligne de la matrice par le vecteur
            dot_product = sum(x * y for x, y in zip(row, b.values))
            result_values.append(dot_product)

        return Vector(result_values)

    # Cas Matrice * Matrice
    if isinstance(a, Matrix) and isinstance(b, Matrix):
        rows_a, cols_a = a.shape()
        rows_b, cols_b = b.shape()

        if cols_a != rows_b:
            raise ValueError("Matrix A columns must match Matrix B rows.")

        result_values = []
        for i in range(rows_a):
            result_row = []
            for j in range(cols_b):
                # Calculer l'élément [i][j]
                value = sum(
                    a.values[i][k] * b.values[k][j] for k in range(cols_a)
                )
                result_row.append(value)
            result_values.append(result_row)

        return Matrix(result_values)

    raise TypeError(
        "Unsupported types for matmul. Must be Matrix*Vector or Matrix*Matrix."
    )
