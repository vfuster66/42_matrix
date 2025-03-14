from ex01.linear_combination import linear_combination
from ex00.vector import Vector
from printer import Printer


def main():
    printer = Printer()
    printer.header("DEMO - Ex01: Linear Combination")

    printer.title("Linear Combination of Basis Vectors (e1, e2, e3)")
    e1 = Vector([1.0, 0.0, 0.0])
    e2 = Vector([0.0, 1.0, 0.0])
    e3 = Vector([0.0, 0.0, 1.0])

    coefs = [10.0, -2.0, 0.5]
    result = linear_combination([e1, e2, e3], coefs)
    printer.print_vector(
        result, label="Resulting Vector (10*e1 - 2*e2 + 0.5*e3)"
    )

    printer.title("Linear Combination of Custom Vectors (v1, v2)")
    v1 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([0.0, 10.0, -100.0])

    coefs = [10.0, -2.0]
    result = linear_combination([v1, v2], coefs)
    printer.print_vector(result, label="Resulting Vector (10*v1 - 2*v2)")

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
