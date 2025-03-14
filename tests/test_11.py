from ex11.determinant import determinant
from ex00.matrix import Matrix
from printer import Printer


def isclose(a, b, rel_tol=1e-9):
    return abs(a - b) <= rel_tol * max(abs(a), abs(b), 1.0)


def test_determinant_2x2():
    printer = Printer()
    printer.section("Determinant 2x2 Matrix")

    m = Matrix([[4, 6], [3, 8]])
    result = determinant(m)

    printer.info(f"det(m): {result}")
    assert isclose(result, 14)


def test_determinant_3x3():
    printer = Printer()
    printer.section("Determinant 3x3 Matrix")

    m = Matrix([
        [6, 1, 1],
        [4, -2, 5],
        [2, 8, 7]
    ])
    result = determinant(m)

    printer.info(f"det(m): {result}")
    assert isclose(result, -306)


def test_determinant_non_square():
    printer = Printer()
    printer.section("Determinant of Non Square Matrix")

    m = Matrix([
        [1, 2, 3],
        [4, 5, 6]
    ])

    try:
        determinant(m)
        assert False, "Expected ValueError for non-square matrix"
    except ValueError as e:
        printer.error(str(e))
        assert str(e) == "Determinant is only defined for square matrices."
