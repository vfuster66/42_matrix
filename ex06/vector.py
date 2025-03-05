class Vector:
    """Classe représentant un vecteur."""

    def __init__(self, values):
        """Initialise un vecteur avec une liste de nombres valides."""
        if not isinstance(values, list):
            raise TypeError(
                "Vector doit être initialisé avec une liste de nombres."
            )

        for v in values:
            if not isinstance(v, (int, float)):
                raise TypeError(
                    f"Vector ne peut contenir que des nombres valides, "
                    f"trouvé : {v}"
                    )

        self.values = values

    def cross_product(self, v):
        """Produit vectoriel entre deux vecteurs en 3D.

        Args:
            v (Vector): Deuxième vecteur.

        Returns:
            Vector: Résultat du produit vectoriel.

        Raises:
            ValueError: Si les vecteurs ne sont pas en 3D.
        """
        if len(self.values) != 3 or len(v.values) != 3:
            raise ValueError(
                "Le produit vectoriel est défini pour les vecteurs en 3D."
            )

        u1, u2, u3 = self.values
        v1, v2, v3 = v.values

        return Vector([
            u2 * v3 - u3 * v2,
            u3 * v1 - u1 * v3,
            u1 * v2 - u2 * v1
        ])

    def __repr__(self):
        """Représentation textuelle du vecteur."""
        return f"Vector({self.values})"
