from math import tan
from ex00.matrix import Matrix
from printer import Printer

# Constante pi
PI = 3.141592653589793


def degrees_to_radians(degrees):
    """Convertit des degrés en radians."""
    return degrees * (PI / 180)


def isclose_matrix(m1, m2, rel_tol=1e-9):
    """Compare deux matrices avec une tolérance sur les floats."""
    for row1, row2 in zip(m1.values, m2.values):
        for a, b in zip(row1, row2):
            if abs(a - b) > rel_tol * max(abs(a), abs(b), 1.0):
                return False
    return True


def test_projection_matrix():
    printer = Printer()
    printer.section("Projection Perspective Matrix 4x4")

    # ➤ Paramètres
    fov_deg = 90
    fov_rad = degrees_to_radians(fov_deg)
    f = 1.0 / tan(fov_rad / 2)

    ratio = 16 / 9
    near = 1.0
    far = 500.0

    # ➤ Génération de la matrice
    P = Matrix.projection(f, ratio, near, far)

    # ➤ Matrice attendue calculée à la main
    nf = 1 / (near - far)
    a = (far + near) * nf
    b = (2 * far * near) * nf

    expected = Matrix([
        [f / ratio, 0.0, 0.0, 0.0],
        [0.0, f, 0.0, 0.0],
        [0.0, 0.0, a, b],
        [0.0, 0.0, -1.0, 0.0]
    ])

    assert isclose_matrix(P, expected)
    printer.success("Projection perspective matrix generated successfully ✅")


def test_to_column_major():
    printer = Printer()
    printer.section("Column Major Projection Matrix")

    # ➤ Paramètres
    fov_deg = 90
    fov_rad = degrees_to_radians(fov_deg)
    f = 1.0 / tan(fov_rad / 2)

    ratio = 16 / 9
    near = 1.0
    far = 500.0

    # ➤ Génération de la matrice
    P = Matrix.projection(f, ratio, near, far)
    col_major = P.to_column_major()

    # ➤ Vérification simple ➔ dimension correcte
    assert col_major.shape() == (4, 4)
    printer.success("Column major conversion successful ✅")
