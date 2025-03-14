from ex00.vector import Vector


def angle_cos(u: Vector, v: Vector) -> float:
    """Retourne le cosinus de l'angle entre deux vecteurs u et v."""

    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise TypeError("Both inputs must be Vectors.")

    if u.size() != v.size():
        raise ValueError("Vectors must have the same size.")

    norm_u = u.norm()
    norm_v = v.norm()

    if norm_u == 0 or norm_v == 0:
        raise ValueError("Cannot compute cosine with zero-length vector.")

    return u.dot(v) / (norm_u * norm_v)
