from ex00.vector import Vector
from printer import Printer


def main():
    printer = Printer()
    printer.header("DEMO - Ex04: Norms")

    u = Vector([1.0, 2.0, 3.0])
    printer.title("Norm 1")
    result = u.norm_1()
    printer.info(f"norm_1(u): {result}")

    printer.title("Norm 2 (Euclidean)")
    result = u.norm()
    printer.info(f"norm(u): {result}")

    printer.title("Norm Infinity")
    result = u.norm_inf()
    printer.info(f"norm_inf(u): {result}")

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
