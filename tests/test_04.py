from ex00.vector import Vector
from printer import Printer


def isclose(a, b, rel_tol=1e-9):
    return abs(a - b) <= rel_tol * max(abs(a), abs(b), 1.0)


def test_norm_zero():
    printer = Printer()
    printer.section("Norm of Zero Vector")

    u = Vector([0.0, 0.0, 0.0])
    assert isclose(u.norm_1(), 0.0)
    assert isclose(u.norm(), 0.0)
    assert isclose(u.norm_inf(), 0.0)


def test_norm_positive():
    printer = Printer()
    printer.section("Norm of [1.0, 2.0, 3.0]")

    u = Vector([1.0, 2.0, 3.0])

    assert isclose(u.norm_1(), 6.0)
    assert isclose(u.norm(), 3.74165738677)
    assert isclose(u.norm_inf(), 3.0)


def test_norm_negative():
    printer = Printer()
    printer.section("Norm of [-1.0, -2.0]")

    u = Vector([-1.0, -2.0])

    assert isclose(u.norm_1(), 3.0)
    assert isclose(u.norm(), 2.2360679775)
    assert isclose(u.norm_inf(), 2.0)
