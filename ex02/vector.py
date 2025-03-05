class Vector:
    """Classe représentant un vecteur."""

    def __init__(self, values):
        if not isinstance(values, list) or not all(
            isinstance(v, (int, float)) for v in values
        ):
            raise TypeError(
                "Vector doit être initialisé avec une liste de nombres."
            )
        self.values = values

    def __repr__(self):
        return f"Vector({self.values})"

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return all(
            abs(a - b) < 1e-6 for a, b in zip(self.values, other.values)
        )
