from ex00.matrix import Matrix


def determinant(matrix: Matrix) -> float:
    """Retourne le déterminant d'une matrice carrée (jusqu'à 4x4)."""
    rows, cols = matrix.shape()

    if rows != cols:
        raise ValueError("Determinant is only defined for square matrices.")

    # Cas de base 1x1
    if rows == 1:
        return matrix.values[0][0]

    # Cas de base 2x2
    if rows == 2:
        a, b = matrix.values[0]
        c, d = matrix.values[1]
        return a * d - b * c

    # Pour n > 2 : par row echelon
    mat = matrix.copy()
    n = rows
    A = mat.values
    det = 1
    sign = 1

    for i in range(n):
        # Recherche du pivot
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if A[max_row][i] == 0:
            return 0

        # Échange si nécessaire
        if i != max_row:
            A[i], A[max_row] = A[max_row], A[i]
            sign *= -1

        # Produit diagonal
        det *= A[i][i]

        # Elimination
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            A[j] = [a - factor * b for a, b in zip(A[j], A[i])]

    return det * sign
