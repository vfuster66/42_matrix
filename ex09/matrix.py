class Matrix:
    """Classe représentant une matrice."""

    def __init__(self, values):
        """Initialise une matrice avec une liste de listes."""
        if not isinstance(values, list) or not all(
            isinstance(row, list) for row in values
        ):
            raise TypeError("Matrix doit être une liste de listes.")

        if len(values) == 0:
            self.values = []
            return

        row_length = len(values[0])
        if any(len(row) != row_length for row in values):
            raise ValueError(
                "Toutes les lignes doivent avoir la même longueur."
                )

        self.values = values

    def transpose(self):
        """Retourne la transposée de la matrice."""
        if not self.values:
            return Matrix([])

        transposed_values = [
            [self.values[j][i] for j in range(len(self.values))]
            for i in range(len(self.values[0]))
        ]
        return Matrix(transposed_values)

    def __repr__(self):
        return f"Matrix({self.values})"
