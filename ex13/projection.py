from ex00.vector import Vector
from ex00.matrix import Matrix


def projection_matrix(u: Vector) -> Matrix:
    """Retourne la matrice de projection orthogonale sur le vecteur u."""

    if u.norm() == 0:
        raise ValueError("Cannot compute projection for zero vector.")

    # Outer product : u @ u.T
    outer = [[ui * uj for uj in u.values] for ui in u.values]

    # Norm squared
    norm_sq = u.dot(u)

    # Multiply by 1 / (u . u)
    proj = [[val / norm_sq for val in row] for row in outer]

    return Matrix(proj)
