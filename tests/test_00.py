from ex00.vector import Vector
from ex00.matrix import Matrix
from printer import Printer


def test_vector_add():
    p = Printer()
    v1 = Vector([2.0, 3.0])
    v2 = Vector([5.0, 7.0])
    v1.add(v2)
    p.section("Vector Addition")
    p.print_vector(v1)
    assert v1.values == [7.0, 10.0]


def test_vector_sub():
    p = Printer()
    v1 = Vector([2.0, 3.0])
    v2 = Vector([5.0, 7.0])
    v1.sub(v2)
    p.section("Vector Subtraction")
    p.print_vector(v1)
    assert v1.values == [-3.0, -4.0]


def test_vector_scl():
    p = Printer()
    v1 = Vector([2.0, 3.0])
    v1.scl(2.0)
    p.section("Vector Scaling")
    p.print_vector(v1)
    assert v1.values == [4.0, 6.0]


def test_matrix_add():
    p = Printer()
    m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
    m2 = Matrix([[7.0, 4.0], [-2.0, 2.0]])
    m1.add(m2)
    p.section("Matrix Addition")
    p.print_matrix(m1)
    assert m1.values == [[8.0, 6.0], [1.0, 6.0]]


def test_matrix_sub():
    p = Printer()
    m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
    m2 = Matrix([[7.0, 4.0], [-2.0, 2.0]])
    m1.sub(m2)
    p.section("Matrix Subtraction")
    p.print_matrix(m1)
    assert m1.values == [[-6.0, -2.0], [5.0, 2.0]]


def test_matrix_scl():
    p = Printer()
    m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
    m1.scl(2.0)
    p.section("Matrix Scaling")
    p.print_matrix(m1)
    assert m1.values == [[2.0, 4.0], [6.0, 8.0]]


def main():
    test_vector_add()
    test_vector_sub()
    test_vector_scl()
    test_matrix_add()
    test_matrix_sub()
    test_matrix_scl()


if __name__ == "__main__":
    main()
