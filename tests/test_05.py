from ex05.cosine import angle_cos
from ex00.vector import Vector
from printer import Printer


def isclose(a, b, rel_tol=1e-9):
    return abs(a - b) <= rel_tol * max(abs(a), abs(b), 1.0)


def test_parallel_vectors():
    printer = Printer()
    printer.section("Parallel Vectors")

    u = Vector([1.0, 0.0])
    v = Vector([1.0, 0.0])

    result = angle_cos(u, v)
    printer.info(f"cos(u, v): {result}")

    assert isclose(result, 1.0)


def test_orthogonal_vectors():
    printer = Printer()
    printer.section("Orthogonal Vectors")

    u = Vector([1.0, 0.0])
    v = Vector([0.0, 1.0])

    result = angle_cos(u, v)
    printer.info(f"cos(u, v): {result}")

    assert isclose(result, 0.0)


def test_opposite_vectors():
    printer = Printer()
    printer.section("Opposite Vectors")

    u = Vector([-1.0, 1.0])
    v = Vector([1.0, -1.0])

    result = angle_cos(u, v)
    printer.info(f"cos(u, v): {result}")

    assert isclose(result, -1.0)


def test_colinear_vectors():
    printer = Printer()
    printer.section("Colinear Vectors")

    u = Vector([2.0, 1.0])
    v = Vector([4.0, 2.0])

    result = angle_cos(u, v)
    printer.info(f"cos(u, v): {result}")

    assert isclose(result, 1.0)
