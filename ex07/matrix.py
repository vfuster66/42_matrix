from ex07.vector import Vector


class Matrix:
    """Classe représentant une matrice."""

    def __init__(self, values):
        """Initialise une matrice avec une liste de listes."""
        if not isinstance(values, list) or not all(
            isinstance(row, list) for row in values
        ):
            raise TypeError(
                "Matrix doit être initialisée avec une liste de listes."
            )

        if len(values) == 0 or any(
            len(row) != len(values[0]) for row in values
        ):
            raise ValueError(
                "Toutes les lignes de la matrice doivent avoir la même "
                "longueur."
            )

        self.values = values
        self.rows = len(values)
        self.cols = len(values[0])

    def mul_vec(self, vec):
        """Multiplie la matrice par un vecteur."""
        if self.cols != len(vec.values):
            raise ValueError(
                "Le nombre de colonnes de la matrice doit être égal "
                "à la taille du vecteur."
                )

        result = [
            sum(self.values[i][j] * vec.values[j] for j in range(self.cols))
            for i in range(self.rows)
        ]
        return Vector(result)

    def mul_mat(self, mat):
        """Multiplie la matrice par une autre matrice."""
        if self.cols != mat.rows:
            raise ValueError(
                "Le nombre de colonnes de la première matrice doit être égal"
                "au nombre de lignes de la deuxième."
                )

        result = [
            [
                sum(self.values[i][k] * mat.values[k][j]
                    for k in range(self.cols))
                for j in range(mat.cols)
            ]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __repr__(self):
        return f"Matrix({self.values})"
