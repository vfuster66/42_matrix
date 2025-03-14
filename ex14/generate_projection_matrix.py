from ex00.matrix import Matrix
from math import tan

# Définition de π et conversion
PI = 3.141592653589793


def degrees_to_radians(degrees):
    return degrees * (PI / 180)


# Paramètres
fov_deg = 90
fov_rad = degrees_to_radians(fov_deg)
f = 1.0 / tan(fov_rad / 2)

ratio = 16 / 9
near = 1.0
far = 500.0

# Génération de la matrice de projection
projection_matrix = Matrix.projection(f, ratio, near, far)

# Sauvegarde dans le fichier "proj"
projection_matrix.to_column_major().save_to_file("proj")

print("✅ Matrice de projection enregistrée dans 'proj'.")
