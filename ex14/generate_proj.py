from math import tan
from ex00.matrix import Matrix

# Constante pi
PI = 3.141592653589793


def degrees_to_radians(degrees):
    """Convertit des degrés en radians sans utiliser math.radians()."""
    return degrees * (PI / 180)


def main():
    # Paramètres de la projection
    fov_deg = 90  # Champ de vision en degrés
    fov_rad = degrees_to_radians(fov_deg)
    f = 1.0 / tan(fov_rad / 2)

    ratio = 16 / 9
    near = 1.0
    far = 500.0

    # Génération de la matrice de projection perspective
    projection_matrix = Matrix.projection(f, ratio, near, far)

    # Sauvegarde dans le fichier "proj"
    projection_matrix.to_column_major().save_to_file("proj")

    print("✅ Matrice de projection enregistrée dans 'proj'.")


if __name__ == "__main__":
    main()
