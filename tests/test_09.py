from ex09.transpose import transpose
from ex00.matrix import Matrix
from printer import Printer


def test_transpose_rectangular():
    printer = Printer()
    printer.section("Transpose 3x2 Matrix ➔ 2x3")

    m = Matrix([
        [1, 2],
        [3, 4],
        [5, 6]
    ])

    result = transpose(m)
    printer.print_matrix(result, label="Transpose(m)")

    expected = Matrix([
        [1, 3, 5],
        [2, 4, 6]
    ])

    assert result == expected


def test_transpose_square():
    printer = Printer()
    printer.section("Transpose 3x3 Matrix")

    m = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    result = transpose(m)
    printer.print_matrix(result, label="Transpose(m)")

    expected = Matrix([
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ])

    assert result == expected
