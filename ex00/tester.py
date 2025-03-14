from ex00.vector import Vector
from ex00.matrix import Matrix
from printer import Printer


def main():
    printer = Printer()
    printer.header("DEMO - Ex00: Add, Subtract and Scale")

    # ➤ Vector Add
    printer.title("Vector Addition")
    v1 = Vector([2.0, 3.0])
    v2 = Vector([5.0, 7.0])
    v1.add(v2)
    printer.print_vector(v1, label="v1 + v2")

    # ➤ Vector Subtract
    printer.title("Vector Subtraction")
    v3 = Vector([2.0, 3.0])
    v4 = Vector([5.0, 7.0])
    v3.sub(v4)
    printer.print_vector(v3, label="v3 - v4")

    # ➤ Vector Scaling
    printer.title("Vector Scaling")
    v5 = Vector([2.0, 3.0])
    v5.scl(2.0)
    printer.print_vector(v5, label="v5 * 2")

    # ➤ Matrix Add
    printer.title("Matrix Addition")
    m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
    m2 = Matrix([[7.0, 4.0], [-2.0, 2.0]])
    m1.add(m2)
    printer.print_matrix(m1, label="m1 + m2")

    # ➤ Matrix Subtract
    printer.title("Matrix Subtraction")
    m3 = Matrix([[1.0, 2.0], [3.0, 4.0]])
    m4 = Matrix([[7.0, 4.0], [-2.0, 2.0]])
    m3.sub(m4)
    printer.print_matrix(m3, label="m3 - m4")

    # ➤ Matrix Scaling
    printer.title("Matrix Scaling")
    m5 = Matrix([[1.0, 2.0], [3.0, 4.0]])
    m5.scl(2.0)
    printer.print_matrix(m5, label="m5 * 2")

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
