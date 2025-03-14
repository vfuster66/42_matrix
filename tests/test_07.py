from ex07.matrix_multiplication import matmul
from ex00.matrix import Matrix
from ex00.vector import Vector
from printer import Printer


def test_matmul_matrix_vector():
    printer = Printer()
    printer.section("Matrix * Vector")

    m = Matrix([[1, 2], [3, 4], [5, 6]])
    v = Vector([7, 8])

    result = matmul(m, v)
    printer.print_vector(result, label="m * v")

    assert result == Vector([23, 53, 83])


def test_matmul_matrix_matrix():
    printer = Printer()
    printer.section("Matrix * Matrix")

    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    m2 = Matrix([[7, 8], [9, 10], [11, 12]])

    result = matmul(m1, m2)
    printer.print_matrix(result, label="m1 * m2")

    assert result == Matrix([
        [58, 64],
        [139, 154]
    ])
