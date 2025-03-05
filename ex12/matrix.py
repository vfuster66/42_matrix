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
        self.n = len(values[0]) if self.m > 0 else 0  # Nombre de colonnes

        if self.m != self.n:
            raise ValueError(
                "Seules les matrices carrées peuvent être inversées."
                )

    def determinant(self):
        """Calcule le déterminant de la matrice."""
        if self.m == 1:
            return self.values[0][0]

        if self.m == 2:
            return (
                self.values[0][0] * self.values[1][1] -
                self.values[0][1] * self.values[1][0]
            )

        det = 0
        for col in range(self.n):
            minor = [
                [self.values[i][j] for j in range(self.n) if j != col]
                for i in range(1, self.m)
            ]
            det += ((-1) ** col) * self.values[0][col] * \
                Matrix(minor).determinant()

        return det

    def inverse(self):
        """Calcule l'inverse de la matrice en utilisant
        la méthode de Gauss-Jordan."""
        if self.determinant() == 0:
            raise ValueError("La matrice est singulière et n'a pas d'inverse.")

        mat = [
            row[:] + [1 if i == j else 0 for j in range(self.n)]
            for i, row in enumerate(self.values)
        ]
        size = self.n

        for col in range(size):
            max_row = max(range(col, size), key=lambda r: abs(mat[r][col]))
            if abs(mat[max_row][col]) < 1e-10:
                raise ValueError(
                    "La matrice est singulière et n'a pas d'inverse."
                    )

            mat[col], mat[max_row] = mat[max_row], mat[col]

            pivot = mat[col][col]
            mat[col] = [x / pivot for x in mat[col]]

            for row in range(size):
                if row != col:
                    factor = mat[row][col]
                    mat[row] = [
                        x - factor * y for x, y in zip(mat[row], mat[col])
                    ]

        inverse_values = [row[size:] for row in mat]
        return Matrix(inverse_values)

    def __repr__(self):
        """Affichage de la matrice."""
        return f"Matrix({self.values})"
