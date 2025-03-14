from ex01.linear_combination import linear_combination
from ex00.vector import Vector
from printer import Printer


def test_linear_combination_basis_vectors():
    printer = Printer()
    printer.section("Linear Combination - Basis Vectors")

    e1 = Vector([1.0, 0.0, 0.0])
    e2 = Vector([0.0, 1.0, 0.0])
    e3 = Vector([0.0, 0.0, 1.0])

    coefs = [10.0, -2.0, 0.5]
    result = linear_combination([e1, e2, e3], coefs)
    printer.print_vector(result)
    assert result.values == [10.0, -2.0, 0.5]


def test_linear_combination_custom_vectors():
    printer = Printer()
    printer.section("Linear Combination - Custom Vectors")

    v1 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([0.0, 10.0, -100.0])

    coefs = [10.0, -2.0]
    result = linear_combination([v1, v2], coefs)
    printer.print_vector(result)
    assert result.values == [10.0, 0.0, 230.0]
