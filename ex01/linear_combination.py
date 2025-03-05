"""
Module contenant la fonction pour calculer une combinaison linéaire de
vecteurs.
"""

from typing import List
from ex01.vector import Vector


def linear_combination(vectors: List[Vector], coefs: List[float]) -> Vector:
    """Calcule la combinaison linéaire des vecteurs avec les coefficients."""
    if len(vectors) != len(coefs):
        raise ValueError(
            "Les listes de vecteurs et de coefficients "
            "doivent avoir la même taille.")

    if not vectors:
        return Vector([0])

    dim = len(vectors[0].values)
    if any(len(vec.values) != dim for vec in vectors):
        raise ValueError("Tous les vecteurs doivent avoir la même dimension.")

    # Initialisation avec un vecteur nul de même dimension
    result = Vector([0] * dim)

    # Calcul de la combinaison linéaire
    for vec, coef in zip(vectors, coefs):
        result = result + (vec * coef)

    return result
