import copy


class Matrix:
    """Classe représentant une matrice avec les opérations de base."""

    def __init__(self, values):
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

    def shape(self):
        """Retourne (nombre de lignes, nombre de colonnes)."""
        return (len(self.values), len(self.values[0]))

    def copy(self):
        """Retourne une copie profonde de la matrice."""
        return Matrix(copy.deepcopy(self.values))

    def add(self, m):
        if (
            not isinstance(m, Matrix)
            or len(self.values) != len(m.values)
            or len(self.values[0]) != len(m.values[0])
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
        if (
            not isinstance(m, Matrix)
            or len(self.values) != len(m.values)
            or len(self.values[0]) != len(m.values[0])
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
        if not isinstance(a, (int, float)):
            raise TypeError("Scalar must be a number.")
        self.values = [[x * a for x in row] for row in self.values]
        return self

    def transpose(self):
        """Retourne la transposée de la matrice."""
        transposed = list(map(list, zip(*self.values)))
        return Matrix(transposed)

    def to_column_major(self):
        """Transpose la matrice pour respecter
        l'ordre column-major utilisé en OpenGL."""
        rows, cols = self.shape()
        return Matrix([
            [self.values[j][i] for j in range(rows)]
            for i in range(cols)
        ])

    def save_to_file(self, filename="proj"):
        """Enregistre la matrice dans un fichier
        au format attendu par ./display."""
        with open(filename, "w") as f:
            for row in self.values:
                f.write(",".join(f"{val:.6f}" for val in row) + "\n")

    @staticmethod
    def projection(f, ratio, near, far):
        """
        Construit la matrice de projection perspective 4x4.

        Args:
            f (float): 1 / tan(fov / 2)
            ratio (float): Rapport largeur/hauteur.
            near (float): Distance du plan proche.
            far (float): Distance du plan éloigné.

        Returns:
            Matrix: La matrice de projection 4x4.
        """
        nf = 1 / (near - far)
        a = (far + near) * nf
        b = (2 * far * near) * nf

        values = [
            [f / ratio, 0.0,  0.0,  0.0],
            [0.0, f,  0.0,  0.0],
            [0.0, 0.0, a, b],
            [0.0, 0.0, -1.0,  0.0]
        ]

        return Matrix(values)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self.values == other.values

    def __repr__(self):
        return "\n".join(str(row) for row in self.values)
