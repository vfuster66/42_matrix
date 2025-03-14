from ex00.matrix import Matrix


def row_echelon(matrix: Matrix) -> Matrix:
    """Retourne la forme échelonnée par lignes d'une matrice."""
    mat = matrix.copy()
    rows, cols = mat.shape()
    A = mat.values  # accès direct pour modification

    lead = 0
    for r in range(rows):
        if lead >= cols:
            break
        i = r
        while A[i][lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if cols == lead:
                    break
        if lead >= cols:
            break

        # Swap rows i and r
        A[i], A[r] = A[r], A[i]

        lv = A[r][lead]
        if lv != 0:
            A[r] = [m / lv for m in A[r]]

        for i in range(r + 1, rows):
            lv = A[i][lead]
            A[i] = [iv - lv * rv for rv, iv in zip(A[r], A[i])]

        lead += 1

    return Matrix(A)
