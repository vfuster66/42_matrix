from ex10.row_echelon import row_echelon
from ex00.matrix import Matrix
from printer import Printer


def isclose_matrix(m1, m2, rel_tol=1e-9):
    for row1, row2 in zip(m1.values, m2.values):
        for a, b in zip(row1, row2):
            if abs(a - b) > rel_tol * max(abs(a), abs(b), 1.0):
                return False
    return True


def test_row_echelon_simple():
    printer = Printer()
    printer.section("Row Echelon of Simple Matrix")

    m = Matrix([
        [1, 2, -1, -4],
        [2, 3, -1, -11],
        [-2, 0, -3, 22]
    ])

    result = row_echelon(m)
    printer.print_matrix(result, label="Row Echelon Form")

    expected = Matrix([
        [1.0, 2.0, -1.0, -4.0],
        [0.0, 1.0, -1.0, 3.0],
        [0.0, 0.0, 1.0, -2.0]
    ])

    assert isclose_matrix(result, expected)


def test_row_echelon_identity():
    printer = Printer()
    printer.section("Row Echelon of Identity Matrix")

    m = Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    result = row_echelon(m)
    printer.print_matrix(result, label="Row Echelon Form")

    expected = Matrix([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
    ])

    assert isclose_matrix(result, expected)
