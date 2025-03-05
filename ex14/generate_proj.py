import math
from ex14.matrix import Matrix

# Définition des paramètres de la projection
fov = math.radians(90)  # Champ de vision en radians
ratio = 16 / 9          # Rapport largeur/hauteur
near = 1.0             # Plan proche
far = 500.0             # Plan éloigné

# Génération de la matrice de projection
projection_matrix = Matrix.projection(fov, ratio, near, far)

# Sauvegarde dans le fichier "proj"
projection_matrix.to_column_major().save_to_file("proj")

print("✅ Matrice de projection enregistrée dans 'proj'.")
