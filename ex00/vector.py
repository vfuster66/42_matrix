import copy


class Vector:
    """Classe représentant un vecteur avec des opérations
    d'algèbre linéaire."""

    def __init__(self, values):
        """Initialise le vecteur avec une liste de valeurs flottantes."""
        if not isinstance(values, list) or not all(
            isinstance(v, (int, float)) for v in values
        ):
            raise TypeError(
                "Vector must be initialized with a list of numbers."
            )
        if not values:
            raise ValueError("Vector must contain at least one element.")
        self.values = values

    def size(self) -> int:
        """Retourne la taille du vecteur (dimension)."""
        return len(self.values)

    def copy(self):
        """Retourne une copie du vecteur."""
        return Vector(copy.deepcopy(self.values))

    def add(self, v):
        """Additionne un autre vecteur de même taille."""
        if not isinstance(v, Vector) or len(self.values) != len(v.values):
            raise ValueError("Vectors must have the same size for addition.")
        self.values = [x + y for x, y in zip(self.values, v.values)]
        return self

    def sub(self, v):
        """Soustrait un autre vecteur de même taille."""
        if not isinstance(v, Vector) or len(self.values) != len(v.values):
            raise ValueError(
                "Vectors must have the same size for subtraction."
            )
        self.values = [x - y for x, y in zip(self.values, v.values)]
        return self

    def scl(self, a):
        """Multiplie chaque élément du vecteur par un scalaire."""
        if not isinstance(a, (int, float)):
            raise TypeError("Scalar must be a number.")
        self.values = [x * a for x in self.values]
        return self

    def norm_1(self):
        """Norme 1 (somme des valeurs absolues)."""
        return sum(abs(x) for x in self.values)

    def norm(self):
        """Norme 2 (euclidienne)."""
        return sum(x ** 2 for x in self.values) ** 0.5

    def norm_inf(self):
        """Norme infinie (valeur absolue maximale)."""
        return max(abs(x) for x in self.values)

    def dot(self, v):
        """Produit scalaire avec un autre vecteur."""
        if not isinstance(v, Vector) or len(self.values) != len(v.values):
            raise ValueError(
                "Vectors must have the same size for dot product."
            )
        return sum(x * y for x, y in zip(self.values, v.values))

    def __eq__(self, other):
        """Vérifie l'égalité avec un autre vecteur."""
        if not isinstance(other, Vector):
            return False
        return self.values == other.values

    def __repr__(self):
        """Affichage lisible."""
        return f"Vector({self.values})"
