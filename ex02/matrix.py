class Matrix:
    """Classe représentant une matrice."""

    def __init__(self, values):
        if not isinstance(values, list) or not all(
            isinstance(row, list) for row in values
        ):
            raise TypeError(
                "Matrix doit être initialisé avec une liste de listes."
            )
        if not all(len(row) == len(values[0]) for row in values):
            raise ValueError(
                "Toutes les lignes doivent avoir le même nombre de colonnes."
            )
        self.values = values

    def __repr__(self):
        return f"Matrix({self.values})"

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return all(
            all(abs(a - b) < 1e-6 for a, b in zip(row1, row2))
            for row1, row2 in zip(self.values, other.values)
        )
