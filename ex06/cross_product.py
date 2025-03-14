from ex00.vector import Vector


def cross_product(u: Vector, v: Vector) -> Vector:
    """Produit vectoriel entre deux vecteurs en 3D."""
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise TypeError("Both arguments must be Vectors.")

    if u.size() != 3 or v.size() != 3:
        raise ValueError(
            "Cross product is only defined for 3-dimensional vectors."
        )

    u1, u2, u3 = u.values
    v1, v2, v3 = v.values

    result = [
        u2 * v3 - u3 * v2,
        u3 * v1 - u1 * v3,
        u1 * v2 - u2 * v1
    ]

    return Vector(result)
