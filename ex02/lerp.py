from ex00.vector import Vector
from ex00.matrix import Matrix


def lerp(u, v, t: float):
    """Linear interpolation between two vectors or matrices."""

    if type(u) is not type(v):
        raise ValueError("Objects must be of the same type for interpolation.")

    if isinstance(u, Vector):
        values = []
        for x, y in zip(u.values, v.values):
            values.append((1 - t) * x + t * y)
        return Vector(values)

    if isinstance(u, Matrix):
        rows = len(u.values)
        cols = len(u.values[0])

        values = []
        for i in range(rows):
            row = []
            for j in range(cols):
                val = (1 - t) * u.values[i][j] + t * v.values[i][j]
                row.append(val)
            values.append(row)
        return Matrix(values)

    # Cas pour les scalaires
    if isinstance(u, (int, float)):
        return (1 - t) * u + t * v

    raise TypeError("Unsupported type for interpolation.")
