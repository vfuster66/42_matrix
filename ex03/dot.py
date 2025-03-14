from ex00.vector import Vector


def dot(u: Vector, v: Vector) -> float:
    """Produit scalaire entre deux vecteurs."""
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise TypeError("Both arguments must be Vectors.")
    if u.size() != v.size():
        raise ValueError("Vectors must have the same dimension.")
    
    return sum(x * y for x, y in zip(u.values, v.values))
