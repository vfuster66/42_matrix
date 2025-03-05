from ex05.vector import Vector


def angle_cos(u: Vector, v: Vector) -> float:
    """Calcule le cosinus de l'angle entre deux vecteurs.

    Args:
        u (Vector): Premier vecteur.
        v (Vector): Deuxième vecteur.

    Returns:
        float: Cosinus de l'angle entre `u` et `v`.

    Raises:
        ValueError: Si les vecteurs ont des tailles différentes ou sont nuls.
    """
    if len(u.values) != len(v.values):
        raise ValueError("Les vecteurs doivent avoir la même dimension.")

    norm_u = u.norm()
    norm_v = v.norm()

    if norm_u == 0.0 or norm_v == 0.0:
        raise ValueError("Le cosinus est indéfini pour un vecteur nul.")

    # ✅ Normalisation des vecteurs pour réduire les erreurs de précision
    normalized_u = Vector([x / norm_u for x in u.values])
    normalized_v = Vector([x / norm_v for x in v.values])

    # ✅ Produit scalaire après normalisation
    cos_theta = normalized_u.dot(normalized_v)

    # ✅ Correction : S'assurer que cos_theta reste bien dans [-1, 1]
    cos_theta = max(-1.0, min(1.0, cos_theta))

    return cos_theta
