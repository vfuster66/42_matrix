from ex02.lerp import lerp
from ex00.vector import Vector
from ex00.matrix import Matrix
from printer import Printer


def main():
    printer = Printer()
    printer.header("DEMO - Ex02: Linear Interpolation")

    # ➤ Scalar interpolation
    printer.title("Scalar Interpolation (t=0)")
    result = lerp(0.0, 1.0, 0)
    printer.info(f"Result: {result}")

    printer.title("Scalar Interpolation (t=1)")
    result = lerp(0.0, 1.0, 1)
    printer.info(f"Result: {result}")

    printer.title("Scalar Interpolation (t=0.5)")
    result = lerp(0.0, 1.0, 0.5)
    printer.info(f"Result: {result}")

    # ➤ Vector interpolation
    printer.title("Vector Interpolation (t=0.3)")
    u = Vector([2.0, 1.0])
    v = Vector([4.0, 2.0])
    result = lerp(u, v, 0.3)
    printer.print_vector(result)

    # ➤ Matrix interpolation
    printer.title("Matrix Interpolation (t=0.5)")
    m1 = Matrix([[2.0, 1.0], [3.0, 4.0]])
    m2 = Matrix([[20.0, 10.0], [30.0, 40.0]])
    result = lerp(m1, m2, 0.5)
    printer.print_matrix(result)

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
