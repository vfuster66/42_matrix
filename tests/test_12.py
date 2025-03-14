from ex12.inverse import inverse
from ex00.matrix import Matrix
from printer import Printer


def isclose_matrix(m1, m2, rel_tol=1e-9):
    for row1, row2 in zip(m1.values, m2.values):
        for a, b in zip(row1, row2):
            if abs(a - b) > rel_tol * max(abs(a), abs(b), 1.0):
                return False
    return True


def test_inverse_2x2():
    printer = Printer()
    printer.section("Inverse of 2x2 Matrix")

    m = Matrix([[4, 7], [2, 6]])
    inv_m = inverse(m)

    expected = Matrix([[0.6, -0.7], [-0.2, 0.4]])
    assert isclose_matrix(inv_m, expected)


def test_inverse_identity():
    printer = Printer()
    printer.section("Inverse of Identity Matrix")

    m = Matrix([[1, 0], [0, 1]])
    inv_m = inverse(m)

    expected = Matrix([[1, 0], [0, 1]])
    assert isclose_matrix(inv_m, expected)


def test_singular_matrix():
    printer = Printer()
    printer.section("Inverse of Singular Matrix")

    m = Matrix([[1, 2], [2, 4]])
    try:
        inverse(m)
        assert False, "Expected ValueError for singular matrix"
    except ValueError as e:
        printer.error(str(e))
        assert str(e) == "Matrix is singular and cannot be inverted."
