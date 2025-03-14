from math import tan
from ex00.matrix import Matrix
from printer import Printer

# Constante pi
PI = 3.141592653589793


def degrees_to_radians(degrees):
    """Convertit des degrés en radians sans utiliser math.radians()."""
    return degrees * (PI / 180)


def main():
    printer = Printer()
    printer.header("DEMO - Ex14: Generate Projection Matrix")

    # Paramètres
    fov_deg = 90
    fov_rad = degrees_to_radians(fov_deg)
    f = 1.0 / tan(fov_rad / 2)

    ratio = 16 / 9
    near = 1.0
    far = 500.0

    # Génération de la matrice de projection perspective
    projection_matrix = Matrix.projection(f, ratio, near, far)

    printer.title("Projection Matrix")
    printer.print_matrix(projection_matrix, label="Row-major order")

    # Version Column-major pour OpenGL
    col_major = projection_matrix.to_column_major()
    printer.print_matrix(col_major, label="Column-major order")

    # Sauvegarde pour vérification dans display
    col_major.save_to_file("proj")

    printer.success("Projection matrix saved to 'proj'.")
    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
