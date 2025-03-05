from ex02.vector import Vector
from ex02.matrix import Matrix


def is_nan(value):
    """Détecte si une valeur est NaN sans utiliser de bibliothèque externe."""
    return value != value


def lerp(u, v, t):
    """Effectue une interpolation linéaire entre u et v avec un facteur t."""

    if (u != u) or (v != v) or (t != t):  # Vérifie NaN sans `math.isnan()`
        raise ValueError("lerp ne supporte pas NaN")

    if not (0 <= t <= 1):
        raise ValueError("t doit être compris entre 0 et 1")

    if isinstance(u, (int, float)) and isinstance(v, (int, float)):
        return round((1 - t) * u + t * v, 10)

    if isinstance(u, Vector) and isinstance(v, Vector):
        if len(u.values) != len(v.values):
            raise ValueError("Les vecteurs doivent avoir la même taille")
        return Vector([
            round((1 - t) * u_i + t * v_i, 10)
            for u_i, v_i in zip(u.values, v.values)
        ])

    if isinstance(u, Matrix) and isinstance(v, Matrix):
        if (len(u.values) != len(v.values) or
                len(u.values[0]) != len(v.values[0])):
            raise ValueError("Les matrices doivent avoir la même dimension")
        return Matrix([
            [
                round((1 - t) * u_ij + t * v_ij, 10)
                for u_ij, v_ij in zip(row_u, row_v)
            ]
            for row_u, row_v in zip(u.values, v.values)
        ])

    raise TypeError(
        "Les types de u et v doivent être identiques (float, Vector, Matrix)"
    )
