from ex03.vector import Vector


def dot(u, v):
    """Calcule le produit scalaire de deux vecteurs en appelant `Vector.dot()`.

    Args:
        u (Vector): Premier vecteur.
        v (Vector): Deuxième vecteur.

    Returns:
        float: Produit scalaire ⟨u|v⟩.

    Raises:
        TypeError: Si `u` et `v` ne sont pas des instances de `Vector`.
        ValueError: Si les vecteurs n'ont pas la même dimension.
    """
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise TypeError(
            "Les arguments doivent être des instances de `Vector`."
        )

    return u.dot(v)
