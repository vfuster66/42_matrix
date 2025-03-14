from ex02.lerp import lerp
from ex00.vector import Vector
from ex00.matrix import Matrix
from printer import Printer


def isclose(a, b, rel_tol=1e-9):
    """Retourne True si a et b sont proches,
    sans utiliser la librairie math."""
    return abs(a - b) <= rel_tol * max(abs(a), abs(b), 1.0)


def test_lerp_scalar():
    printer = Printer()
    printer.section("Scalar Lerp")

    assert isclose(lerp(0, 1, 0), 0)
    assert isclose(lerp(0, 1, 1), 1)
    assert isclose(lerp(0, 1, 0.5), 0.5)
    assert isclose(lerp(21, 42, 0.3), 27.3)


def test_lerp_vector():
    printer = Printer()
    printer.section("Vector Lerp")

    u = Vector([2.0, 1.0])
    v = Vector([4.0, 2.0])

    result = lerp(u, v, 0.3)
    printer.print_vector(result)

    expected = [2.6, 1.3]
    assert all(isclose(a, b) for a, b in zip(result.values, expected))


def test_lerp_matrix():
    printer = Printer()
    printer.section("Matrix Lerp")

    m1 = Matrix([[2.0, 1.0], [3.0, 4.0]])
    m2 = Matrix([[20.0, 10.0], [30.0, 40.0]])

    result = lerp(m1, m2, 0.5)
    printer.print_matrix(result)

    expected = [[11.0, 5.5], [16.5, 22.0]]
    for res_row, exp_row in zip(result.values, expected):
        assert all(isclose(a, b) for a, b in zip(res_row, exp_row))
