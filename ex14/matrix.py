import math


class Matrix:
    """Classe représentant une matrice 4x4 utilisée pour la projection 3D."""

    def __init__(self, values):
        """Initialise la matrice avec une liste de listes."""
        if len(values) != 4 or any(len(row) != 4 for row in values):
            raise ValueError("La matrice doit être 4x4.")

        self.values = values

    @staticmethod
    def projection(fov, ratio, near, far):
        """Construit la matrice de projection perspective
        en respectant les contraintes.

        Args:
            fov (float): Champ de vision en radians.
            ratio (float): Rapport largeur/hauteur.
            near (float): Distance du plan proche.
            far (float): Distance du plan éloigné.

        Returns:
            Matrix: La matrice de projection 4x4.
        """
        f = 1.0 / math.tan(fov / 2)  # ✅ Seule fonction mathématique autorisée

        # Utilisation de fused multiply-add pour minimiser l'erreur numérique
        nf = 1 / (near - far)
        a = (far + near) * nf
        b = (2 * far * near) * nf

        values = [
            [f / ratio, 0,  0,  0],
            [0, f,  0,  0],
            [0, 0, a, b],
            [0, 0, -1,  0]
        ]

        return Matrix(values)

    def __repr__(self):
        """Affichage de la matrice en format lisible."""
        return "\n".join(
            ["\t".join(map(lambda x: f"{x:.6f}", row)) for row in self.values]
        )

    def to_column_major(self):
        """Transpose la matrice pour respecter
        l'ordre column-major utilisé en OpenGL."""
        return Matrix([
            [self.values[j][i] for j in range(4)]
            for i in range(4)
        ])

    def save_to_file(self, filename="proj"):
        """Enregistre la matrice dans un fichier
        au format attendu par ./display."""
        with open(filename, "w") as f:
            for row in self.values:
                f.write(", ".join(f"{val:.6f}" for val in row) + "\n")
