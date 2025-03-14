from ex15.complex import Complex


class Vector:
    """Classe représentant un vecteur de nombres complexes."""

    def __init__(self, values):
        """Initialise un vecteur avec une
        liste de valeurs (complexes ou réelles)."""
        self.values = values

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.values, other.values)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.values, other.values)])

    def conjugate(self):
        """Retourne le vecteur conjugué de chaque élément."""
        return Vector([x.conjugate() for x in self.values])

    def dot(self, other):
        total = Complex(0, 0)
        for x, y in zip(self.values, other.values):
            total = total + (x * y.conjugate())
        return total

    def norm(self):
        return sum(x.norm() ** 2 for x in self.values) ** 0.5

    def mul_scalar(self, scalar):
        return Vector([x * scalar for x in self.values])

    def lerp(self, other, t):
        return Vector([
            Complex(
                x.real * (1 - t) + y.real * t,
                x.imag * (1 - t) + y.imag * t
            )
            for x, y in zip(self.values, other.values)
        ])

    def cosine_similarity(self, other):
        dot_product = self.dot(other)
        norm_product = self.norm() * other.norm()
        return dot_product.real / norm_product if norm_product != 0 else 0

    def cross_product(self, other):
        if len(self.values) != 3 or len(other.values) != 3:
            raise ValueError(
                "Le produit vectoriel est défini en 3D uniquement."
            )
        a, b, c = self.values
        d, e, f = other.values
        return Vector([
            b * f - c * e,
            c * d - a * f,
            a * e - b * d
        ])

    def __eq__(self, other):
        return isinstance(other, Vector) and self.values == other.values

    def __repr__(self):
        return "[" + ", ".join(map(str, self.values)) + "]"
