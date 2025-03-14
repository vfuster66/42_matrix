from ex03.dot import dot
from ex00.vector import Vector
from printer import Printer


def main():
    printer = Printer()
    printer.header("DEMO - Ex03: Dot Product")

    printer.title("Dot Product of Orthogonal Vectors")
    u = Vector([1.0, 0.0])
    v = Vector([0.0, 1.0])
    result = dot(u, v)
    printer.info(f"dot(u, v): {result}")

    printer.title("Dot Product of Parallel Vectors")
    u = Vector([1.0, 1.0])
    v = Vector([1.0, 1.0])
    result = dot(u, v)
    printer.info(f"dot(u, v): {result}")

    printer.title("Dot Product of Arbitrary Vectors")
    u = Vector([-1.0, 6.0])
    v = Vector([3.0, 2.0])
    result = dot(u, v)
    printer.info(f"dot(u, v): {result}")

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
