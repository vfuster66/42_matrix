from ex13.projection import projection_matrix
from ex00.vector import Vector
from ex00.matrix import Matrix
from printer import Printer


def isclose_matrix(m1, m2, rel_tol=1e-9):
    for row1, row2 in zip(m1.values, m2.values):
        for a, b in zip(row1, row2):
            if abs(a - b) > rel_tol * max(abs(a), abs(b), 1.0):
                return False
    return True


def test_projection_unit_vector():
    printer = Printer()
    printer.section("Projection on Unit Vector [1, 0]")

    u = Vector([1.0, 0.0])
    P = projection_matrix(u)

    expected = Matrix([
        [1.0, 0.0],
        [0.0, 0.0]
    ])

    assert isclose_matrix(P, expected)
    printer.success("Projection matrix on unit vector PASSED ✅")


def test_projection_diagonal_vector():
    printer = Printer()
    printer.section("Projection on Vector [1, 1]")

    u = Vector([1.0, 1.0])
    P = projection_matrix(u)

    expected = Matrix([
        [0.5, 0.5],
        [0.5, 0.5]
    ])

    assert isclose_matrix(P, expected)
    printer.success("Projection matrix on [1,1] PASSED ✅")


def test_projection_zero_vector():
    printer = Printer()
    printer.section("Projection on Zero Vector")

    u = Vector([0.0, 0.0])

    try:
        projection_matrix(u)
        assert False, "Expected ValueError for zero vector"
    except ValueError:
        printer.success("Correctly raised ValueError for zero vector ✅")
