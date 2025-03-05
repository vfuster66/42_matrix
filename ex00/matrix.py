class Matrix:
    """Classe représentant une matrice et supportant des opérations d'addition,
    de soustraction et de multiplication par un scalaire."""

    def __init__(self, values):
        """Initialise la matrice avec une liste de listes de nombres."""
        if not isinstance(values, list) or not all(
            isinstance(row, list) for row in values
        ):
            raise TypeError("Matrix must be initialized with a list of lists.")
        if not values or not all(row for row in values):
            raise ValueError(

                "Matrix must contain at least one row and one column."
                )
        if not all(len(row) == len(values[0]) for row in values):
            raise ValueError("All rows must have the same number of columns.")
        self.values = values

    def add(self, m):
        """Additionne une autre matrice de même dimension."""
        if (
            not isinstance(m, Matrix) or
            len(self.values) != len(m.values) or
            len(self.values[0]) != len(m.values[0])
        ):
            raise ValueError(
                "Matrices must have the same dimensions for addition."
                )
        self.values = [
            [x + y for x, y in zip(row1, row2)]
            for row1, row2 in zip(self.values, m.values)
        ]
        return self

    def sub(self, m):
        """Soustrait une autre matrice de même dimension."""
        if (
            not isinstance(m, Matrix) or
            len(self.values) != len(m.values) or
            len(self.values[0]) != len(m.values[0])
        ):
            raise ValueError(
                "Matrices must have the same dimensions for subtraction."
                )
        self.values = [
            [x - y for x, y in zip(row1, row2)]
            for row1, row2 in zip(self.values, m.values)
        ]
        return self

    def scl(self, a):
        """Multiplie chaque élément de la matrice par un scalaire."""
        if not isinstance(a, (int, float)):
            raise TypeError("Scalar must be a number.")
        self.values = [[x * a for x in row] for row in self.values]
        return self

    def __repr__(self):
        """Affichage amélioré pour une meilleure lisibilité."""
        return "\n".join(str(row) for row in self.values)
