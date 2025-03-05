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
        """Transforme la matrice en forme échelonnée par lignes (REF)."""
        mat = [row[:] for row in self.values]
        rows, cols = self.m, self.n
        pivot_row = 0

        for col in range(cols):
            max_row = max(
                range(pivot_row, rows),
                key=lambda r: abs(mat[r][col]),
                default=pivot_row
            )

            if abs(mat[max_row][col]) < 1e-10:
                continue

            mat[pivot_row], mat[max_row] = mat[max_row], mat[pivot_row]

            pivot = mat[pivot_row][col]
            mat[pivot_row] = [x / pivot for x in mat[pivot_row]]

            for r in range(pivot_row + 1, rows):
                facteur = mat[r][col]
                mat[r] = [
                    x - facteur * y for x, y in zip(mat[r], mat[pivot_row])
                ]

            pivot_row += 1

        return Matrix(mat)

    def rank(self):
        """Calcule le rang de la matrice
        (nombre de lignes non nulles dans la REF)."""
        ref = self.row_echelon().values
        rank = sum(any(abs(x) > 1e-10 for x in row) for row in ref)
        return rank

    def __repr__(self):
        """Affichage de la matrice."""
        return f"Matrix({self.values})"
