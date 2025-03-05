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
        print(f"✅ Vecteur initialisé : {self.values}")

    def dot(self, v):
        """Produit scalaire du vecteur avec un autre."""
        if len(self.values) != len(v.values):
            raise ValueError("Les vecteurs doivent avoir la même dimension.")

        result = sum(u_i * v_i for u_i, v_i in zip(self.values, v.values))
        print(f"🔢 Produit scalaire entre {self.values} et {v.values}: "
              f"{result}")
        return result

    def norm(self):
        """Calcule la norme euclidienne du vecteur."""
        result = (sum(x ** 2 for x in self.values)) ** 0.5
        print(f"📏 Norme de {self.values} : {result}")
        return result

    def __repr__(self):
        return f"Vector({self.values})"
