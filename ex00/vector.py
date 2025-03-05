class Vector:
    """Classe représentant un vecteur et supportant des opérations d'addition,
    de soustraction et de multiplication par un scalaire."""

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

    def __repr__(self):
        """Affichage amélioré pour une meilleure lisibilité."""
        return f"Vector({self.values})"
