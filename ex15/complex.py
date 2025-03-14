class Complex:
    """Représente un nombre complexe sous la forme a + bi."""
    def __init__(self, real: float, imag: float = 0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        return Complex(self.real + other, self.imag)

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        return Complex(self.real - other, self.imag)

    def __neg__(self):
        """Négation d'un nombre complexe."""
        return Complex(-self.real, -self.imag)

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.imag * other.imag,
                           self.real * other.imag + self.imag * other.real)
        return Complex(self.real * other, self.imag * other)

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denom = other.real ** 2 + other.imag ** 2
            real_part = (self.real * other.real + self.imag * other.imag) / \
                denom
            imag_part = (self.imag * other.real - self.real * other.imag) / \
                denom
            return Complex(real_part, imag_part)
        return Complex(self.real / other, self.imag / other)

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def norm(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def hermitian_dot(u, v):
        """Produit hermitien : <u|v> = conj(u) · v"""
        if len(u) != len(v):
            raise ValueError("Les vecteurs doivent avoir la même taille.")
        return sum(a.conjugate() * b for a, b in zip(u, v))

    def conjugate_vector(v):
        """Retourne le vecteur conjugué de chaque élément du vecteur `v`."""
        return [x.conjugate() for x in v]

    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.real == other.real and self.imag == other.imag
        return False

    def __repr__(self):
        if self.imag >= 0:
            return f"({self.real} + {self.imag}i)"
        else:
            return f"({self.real} - {abs(self.imag)}i)"
