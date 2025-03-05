def is_nan(value):
    """Détecte si une valeur est NaN sans utiliser de bibliothèque externe."""
    return value != value  # Uniquement vrai pour NaN


class Vector:
    """Classe représentant un vecteur."""

    def __init__(self, values):
        """Initialise un vecteur avec une liste de nombres valides.

        Args:
            values (list): Liste de nombres (int ou float).

        Raises:
            TypeError: Si `values` n'est pas une liste ou contient des éléments
                       invalides.
            ValueError: Si `values` contient NaN.
        """
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
            if is_nan(v):
                raise ValueError(
                    f"Vector ne peut pas contenir NaN, trouvé : {v}"
                )

        self.values = values

    def dot(self, v):
        """Produit scalaire du vecteur avec un autre.

        Args:
            v (Vector): Deuxième vecteur.

        Returns:
            float: Produit scalaire ⟨u|v⟩.

        Raises:
            ValueError: Si les vecteurs n'ont pas la même dimension
            ou sont vides.
        """
        if len(self.values) == 0 or len(v.values) == 0:
            raise ValueError("Les vecteurs ne peuvent pas être vides.")

        if len(self.values) != len(v.values):
            raise ValueError("Les vecteurs doivent avoir la même dimension.")

        return sum(u_i * v_i for u_i, v_i in zip(self.values, v.values))

    def __repr__(self):
        """Représentation textuelle du vecteur."""
        return f"Vector({self.values})"
