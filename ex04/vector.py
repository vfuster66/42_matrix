class Vector:
    """Classe représentant un vecteur et calculant ses normes."""

    def __init__(self, values):
        """Initialise un vecteur avec une liste de nombres valides.

        Args:
            values (list): Liste de nombres (int ou float).

        Raises:
            TypeError: Si `values` n'est pas une liste ou
            contient des éléments invalides.
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
            if v != v:
                raise ValueError(
                    f"Vector ne peut pas contenir NaN, trouvé : {v}"
                )

        self.values = values

    def norm_1(self):
        """Calcule la norme 1 (Manhattan) du vecteur.

        Returns:
            float: Somme des valeurs absolues des coordonnées.
        """
        return sum(v if v >= 0 else -v for v in self.values)

    def norm(self):
        """Calcule la norme 2 (Euclidienne) du vecteur.

        Returns:
            float: Racine carrée de la somme des carrés des coordonnées.
        """
        return (sum(v * v for v in self.values)) ** 0.5

    def norm_inf(self):
        """Calcule la norme infinie (Supremum) du vecteur.

        Returns:
            float: Valeur absolue maximale des coordonnées.
        """
        return (
            max(v if v >= 0 else -v for v in self.values)
            if self.values
            else 0.0
        )

    def __repr__(self):
        """Représentation textuelle du vecteur."""
        return f"Vector({self.values})"
