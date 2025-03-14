from ex00.vector import Vector


def linear_combination(vectors: list[Vector], coefs: list[float]) -> Vector:
    if len(vectors) != len(coefs):
        raise ValueError(
            "Vectors and coefficients lists must be of same length"
        )

    # Initialisation d'un vecteur nul de la bonne taille
    dim = vectors[0].size()
    result_values = [0.0] * dim

    for vector, coef in zip(vectors, coefs):
        if vector.size() != dim:
            raise ValueError("All vectors must have the same dimension")
        # Ajout de chaque composante multipliée par le coefficient
        for i in range(dim):
            result_values[i] += vector.values[i] * coef

    return Vector(result_values)
