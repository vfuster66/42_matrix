from ex03.dot import dot
from ex00.vector import Vector
from printer import Printer


def isclose(a, b, rel_tol=1e-9):
    return abs(a - b) <= rel_tol * max(abs(a), abs(b), 1.0)


def test_dot_zero():
    printer = Printer()
    printer.section("Dot Product - Zero Vectors")

    u = Vector([0.0, 0.0])
    v = Vector([1.0, 1.0])

    result = dot(u, v)
    printer.info(f"dot(u, v): {result}")
    assert isclose(result, 0.0)


def test_dot_parallel():
    printer = Printer()
    printer.section("Dot Product - Parallel Vectors")

    u = Vector([1.0, 1.0])
    v = Vector([1.0, 1.0])

    result = dot(u, v)
    printer.info(f"dot(u, v): {result}")
    assert isclose(result, 2.0)


def test_dot_arbitrary():
    printer = Printer()
    printer.section("Dot Product - Arbitrary Vectors")

    u = Vector([-1.0, 6.0])
    v = Vector([3.0, 2.0])

    result = dot(u, v)
    printer.info(f"dot(u, v): {result}")
    assert isclose(result, 9.0)
