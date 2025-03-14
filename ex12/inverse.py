from ex00.matrix import Matrix
import copy


def inverse(matrix: Matrix) -> Matrix:
    """Retourne l'inverse d'une matrice carrée en utilisant Gauss-Jordan."""

    rows, cols = matrix.shape()

    if rows != cols:
        raise ValueError("Inverse is only defined for square matrices.")

    n = rows
    A = copy.deepcopy(matrix.values)
    identity_matrix = [[float(i == j) for j in range(n)] for i in range(n)]

    for i in range(n):
        # Recherche du pivot
        pivot = A[i][i]
        if pivot == 0:
            # Recherche d'une ligne pour échanger
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    identity_matrix[i], identity_matrix[j] = (
                        identity_matrix[j], identity_matrix[i]
                    )
                    pivot = A[i][i]
                    break
            else:
                raise ValueError("Matrix is singular and cannot be inverted.")

        # Normalisation de la ligne
        A[i] = [x / pivot for x in A[i]]
        identity_matrix[i] = [x / pivot for x in identity_matrix[i]]

        # Elimination sur les autres lignes
        for j in range(n):
            if j != i:
                factor = A[j][i]
                A[j] = [a - factor * b for a, b in zip(A[j], A[i])]
                identity_matrix[j] = [
                    a - factor * b
                    for a, b in zip(identity_matrix[j], identity_matrix[i])
                ]

    return Matrix(identity_matrix)
