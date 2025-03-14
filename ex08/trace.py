from ex00.matrix import Matrix


def trace(matrix: Matrix) -> float:
    """Retourne la trace d'une matrice carrée."""
    rows, cols = matrix.shape()

    if rows != cols:
        raise ValueError("Trace is only defined for square matrices.")

    return sum(matrix.values[i][i] for i in range(rows))
