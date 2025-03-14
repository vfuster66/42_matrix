from ex15.complex import Complex

class Matrix:
    """Classe représentant une matrice de nombres complexes."""

    def __init__(self, values):
        """Initialise une matrice avec une liste de listes de nombres complexes."""
        self.values = values
        self.rows = len(values)
        self.cols = len(values[0]) if self.rows > 0 else 0

    def __eq__(self, other):
        return isinstance(other, Matrix) and self.values == other.values

    def __add__(self, other):
        """Addition de matrices complexes."""
        return Matrix([
            [self.values[i][j] + other.values[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def __sub__(self, other):
        """Soustraction de matrices complexes."""
        return Matrix([
            [self.values[i][j] - other.values[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def mul_scalar(self, scalar):
        """Multiplication par un scalaire complexe."""
        return Matrix([
            [self.values[i][j] * scalar for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def mul_mat(self, other):
        """Multiplication de matrices complexes."""
        if self.cols != other.rows:
            raise ValueError("Multiplication impossible : dimensions incompatibles.")
        
        result = [[Complex(0, 0) for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.values[i][k] * other.values[k][j]
        return Matrix(result)

    def conjugate_transpose(self):
        """Transpose et conjugue la matrice."""
        return Matrix([
            [self.values[j][i].conjugate() for j in range(self.rows)]
            for i in range(self.cols)
        ])

    def trace(self):
        """Calcule la trace de la matrice."""
        return sum(
            (self.values[i][i] for i in range(min(self.rows, self.cols))),
            Complex(0, 0)
        )

    def determinant(self):
        """Calcule le déterminant d'une matrice carrée."""
        if self.rows != self.cols:
            raise ValueError("Le déterminant est défini pour les matrices carrées.")

        if self.rows == 1:
            return self.values[0][0]

        if self.rows == 2:  # Cas 2x2
            a, b = self.values[0]
            c, d = self.values[1]
            return a * d - b * c

        det = Complex(0, 0)
        for col in range(self.cols):
            minor = [
                [self.values[i][j] for j in range(self.cols) if j != col]
                for i in range(1, self.rows)
            ]
            sign = Complex((-1) ** col, 0)
            det += sign * self.values[0][col] * Matrix(minor).determinant()

        return det

    def inverse(self):
        """Calcule l'inverse d'une matrice en utilisant la méthode appropriée."""
        det = self.determinant()
        if det == Complex(0, 0):
            raise ValueError("La matrice est singulière et n'a pas d'inverse.")
        
        # Cas spécifique pour matrice 2x2
        if self.rows == 2:
            a, b = self.values[0]
            c, d = self.values[1]
            inv_det = Complex(1, 0) / det
            return Matrix([
                [d * inv_det, -b * inv_det],
                [-c * inv_det, a * inv_det]
            ])
        
        # Cas général pour matrice NxN
        n = self.rows
        augmented = []
        for i in range(n):
            row = self.values[i].copy()
            identity_row = [Complex(0, 0)] * n
            identity_row[i] = Complex(1, 0)
            row.extend(identity_row)
            augmented.append(row)

        for i in range(n):
            max_row = i
            for k in range(i + 1, n):
                if abs(augmented[k][i].real) + abs(augmented[k][i].imag) > \
                   abs(augmented[max_row][i].real) + abs(augmented[max_row][i].imag):
                    max_row = k

            if augmented[max_row][i] == Complex(0, 0):
                raise ValueError("La matrice est singulière et n'a pas d'inverse.")

            if max_row != i:
                augmented[i], augmented[max_row] = augmented[max_row], augmented[i]

            pivot = augmented[i][i]
            for j in range(2*n):
                augmented[i][j] = augmented[i][j] / pivot

            for k in range(n):
                if k != i:
                    factor = augmented[k][i]
                    for j in range(2*n):
                        augmented[k][j] = augmented[k][j] - factor * augmented[i][j]

        inverse = []
        for i in range(n):
            inverse.append(augmented[i][n:])

        return Matrix(inverse)

    def row_echelon(self):
        """Transforme la matrice en forme échelonnée par lignes (REF)."""
        mat = [row[:] for row in self.values]
        rows, cols = self.rows, self.cols
        pivot_row = 0
        epsilon = 1e-10

        for col in range(cols):
            max_val = 0
            max_row = -1
            for r in range(pivot_row, rows):
                val = abs(mat[r][col].real) + abs(mat[r][col].imag)
                if val > max_val:
                    max_val = val
                    max_row = r

            if max_val < epsilon:
                continue

            mat[pivot_row], mat[max_row] = mat[max_row], mat[pivot_row]

            pivot = mat[pivot_row][col]
            for c in range(cols):
                mat[pivot_row][c] = mat[pivot_row][c] / pivot

            for r in range(rows):
                if r != pivot_row:
                    factor = mat[r][col]
                    for c in range(cols):
                        mat[r][c] = mat[r][c] - factor * mat[pivot_row][c]

            pivot_row += 1
            if pivot_row >= rows:
                break

        return Matrix(mat)

    def rank(self):
        """Calcule le rang de la matrice après réduction échelonnée."""
        ref = self.row_echelon().values
        rank = 0
        epsilon = 1e-10

        for row in ref:
            if any(
                abs(c.real) > epsilon or abs(c.imag) > epsilon
                for c in row
            ):
                rank += 1

        return rank

    def __repr__(self):
        """Affichage lisible de la matrice."""
        return "\n".join(["\t".join(map(str, row)) for row in self.values])
