class Matrix:
    """Classe représentant une matrice et ses opérations."""

    def __init__(self, values):
        """Initialise une matrice avec une liste de listes."""
        if not isinstance(values, list) or not all(
            isinstance(row, list) for row in values
        ):
            raise TypeError(
                "Matrix doit être initialisée avec une liste de listes."
            )

        self.values = values
        self.m = len(values)
        self.n = len(values[0]) if self.m > 0 else 0

    def row_echelon(self):
        """Transforme la matrice en forme échelonnée par lignes (REF)
        et effectue l'élimination vers le haut si nécessaire (RREF)
        pour les matrices non carrées.
        """
        mat = [row[:] for row in self.values]
        rows, cols = self.m, self.n
        pivot_row = 0
        pivot_cols = []

        for col in range(cols):
            max_row = max(
                range(pivot_row, rows),
                key=lambda r: abs(mat[r][col]),
                default=pivot_row
            )

            if abs(mat[max_row][col]) < 1e-10:
                continue

            if pivot_row != max_row:
                mat[pivot_row], mat[max_row] = mat[max_row], mat[pivot_row]

            pivot_cols.append(col)

            pivot = mat[pivot_row][col]
            for c in range(col, cols):
                mat[pivot_row][c] /= pivot

            for r in range(pivot_row + 1, rows):
                facteur = mat[r][col]
                for c in range(col, cols):
                    mat[r][c] -= facteur * mat[pivot_row][c]

            pivot_row += 1
            if pivot_row >= rows:
                break

        if self.m != self.n:
            for i in range(len(pivot_cols) - 1, -1, -1):
                pc = pivot_cols[i]
                for r in range(i):
                    facteur = mat[r][pc]
                    for c in range(pc, cols):
                        mat[r][c] -= facteur * mat[i][c]

        return Matrix(mat)

    def __repr__(self):
        """Affichage de la matrice."""
        return f"Matrix({self.values})"
