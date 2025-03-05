class Matrix:
    """Classe représentant une matrice."""

    def __init__(self, values):
        """Initialise une matrice avec une liste de listes (tableau 2D)."""
        if not isinstance(values, list) or not all(
            isinstance(row, list) for row in values
        ):
            raise TypeError(
                "Matrix doit être initialisée avec une liste de listes."
            )

        row_length = len(values[0])
        if not all(len(row) == row_length for row in values):
            raise ValueError(
                "Toutes les lignes doivent avoir la même longueur."
            )

        self.values = values
        self.rows = len(values)
        self.cols = len(values[0])

    def trace(self):
        """Calcule la trace de la matrice.

        Returns:
            float: Somme des éléments diagonaux de la matrice.

        Raises:
            ValueError: Si la matrice n'est pas carrée.
        """
        if self.rows != self.cols:
            raise ValueError(
                "La trace n'est définie que pour les matrices carrées."
                )

        return sum(self.values[i][i] for i in range(self.rows))

    def __repr__(self):
        """Affichage formaté de la matrice."""
        return f"Matrix({self.values})"
