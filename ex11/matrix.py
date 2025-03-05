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

        if self.m != self.n:
            raise ValueError(
                "Le déterminant est défini uniquement pour les matrices "
                "carrées."
                )

    def determinant(self):
        """Calcule le déterminant d'une matrice carrée de taille 1×1, 2×2,
        3×3 ou 4×4."""
        if self.m == 1:
            return self.values[0][0]

        if self.m == 2:
            a, b = self.values[0]
            c, d = self.values[1]
            return a * d - b * c

        if self.m == 3:
            a, b, c = self.values[0]
            d, e, f = self.values[1]
            g, h, i = self.values[2]
            return (a * (e * i - f * h)
                    - b * (d * i - f * g)
                    + c * (d * h - e * g))

        if self.m == 4:
            det = 0
            for col in range(4):
                minor = self._submatrix(0, col)
                sign = (-1) ** col
                det += sign * self.values[0][col] * minor.determinant()
            return det  # Expansion de Laplace

        raise ValueError(
            "Le calcul du déterminant est limité aux matrices 4×4."
            )

    def _submatrix(self, row, col):
        """Retourne une sous-matrice en supprimant une ligne et une colonne."""
        return Matrix(
            [
                r[:col] + r[col + 1:]
                for i, r in enumerate(self.values)
                if i != row
            ]
        )

    def __repr__(self):
        """Affichage de la matrice."""
        return f"Matrix({self.values})"
