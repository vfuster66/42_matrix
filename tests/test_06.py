from ex06.cross_product import cross_product
from ex00.vector import Vector
from printer import Printer


def test_cross_unit_vectors():
    printer = Printer()
    printer.section("Cross Product of i and j")

    u = Vector([1.0, 0.0, 0.0])
    v = Vector([0.0, 1.0, 0.0])

    result = cross_product(u, v)
    printer.print_vector(result, label="u x v")

    assert result == Vector([0.0, 0.0, 1.0])


def test_cross_opposite_unit_vectors():
    printer = Printer()
    printer.section("Cross Product of j and i")

    u = Vector([0.0, 1.0, 0.0])
    v = Vector([1.0, 0.0, 0.0])

    result = cross_product(u, v)
    printer.print_vector(result, label="u x v")

    assert result == Vector([0.0, 0.0, -1.0])


def test_cross_parallel_vectors():
    printer = Printer()
    printer.section("Cross Product of Parallel Vectors")

    u = Vector([1.0, 2.0, 3.0])
    v = Vector([2.0, 4.0, 6.0])

    result = cross_product(u, v)
    printer.print_vector(result, label="u x v")

    assert result == Vector([0.0, 0.0, 0.0])
