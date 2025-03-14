from ex08.trace import trace
from ex00.matrix import Matrix
from printer import Printer


def isclose(a, b, rel_tol=1e-9):
    return abs(a - b) <= rel_tol * max(abs(a), abs(b), 1.0)


def test_trace_3x3():
    printer = Printer()
    printer.section("Trace of 3x3 Matrix")

    m = Matrix([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]
    ])

    result = trace(m)
    printer.info(f"Trace: {result}")

    assert isclose(result, 15.0)


def test_trace_identity():
    printer = Printer()
    printer.section("Trace of Identity Matrix")

    m = Matrix([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
    ])

    result = trace(m)
    printer.info(f"Trace: {result}")

    assert isclose(result, 3.0)


def test_trace_non_square():
    printer = Printer()
    printer.section("Trace of Non Square Matrix")

    m = Matrix([
        [1.0, 2.0],
        [3.0, 4.0],
        [5.0, 6.0]
    ])

    try:
        trace(m)
        assert False, "Expected ValueError for non-square matrix"
    except ValueError as e:
        printer.error(str(e))
        assert str(e) == "Trace is only defined for square matrices."
