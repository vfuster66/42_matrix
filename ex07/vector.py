class Vector:
    """Classe représentant un vecteur."""

    def __init__(self, values):
        """Initialise un vecteur avec une liste de nombres."""
        if not isinstance(values, list) or not all(isinstance(v, (int, float))
                                                   for v in values):
            raise TypeError(
                "Vector doit être initialisé "
                "avec une liste de nombres valides."
                )

        self.values = values
        self.size = len(values)

    def __repr__(self):
        return f"Vector({self.values})"
