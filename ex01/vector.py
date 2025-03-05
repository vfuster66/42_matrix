from typing import List


class Vector:
    """Représente un vecteur de dimension quelconque."""

    def __init__(self, values: List[float]) -> None:
        if not values:
            raise ValueError("Vector must contain at least one element.")
        self.values = values

    def __add__(self, other: "Vector") -> "Vector":
        if len(self.values) != len(other.values):
            raise ValueError("Les vecteurs doivent avoir la même dimension.")
        return Vector([a + b for a, b in zip(self.values, other.values)])

    def __mul__(self, scalar: float) -> "Vector":
        return Vector([scalar * v for v in self.values])

    def __repr__(self) -> str:
        return "[" + ", ".join(f"{v:.2f}" for v in self.values) + "]"
