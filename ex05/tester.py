from ex05.cosine import angle_cos
from ex00.vector import Vector
from printer import Printer


def main():
    printer = Printer()
    printer.header("DEMO - Ex05: Cosine of Angle Between Vectors")

    # Cas 1 ➔ Vecteurs parallèles
    u = Vector([1.0, 0.0])
    v = Vector([1.0, 0.0])
    printer.title("Parallel Vectors (Expected cos = 1)")
    printer.info(f"cos(u, v): {angle_cos(u, v)}")

    # Cas 2 ➔ Vecteurs orthogonaux
    u = Vector([1.0, 0.0])
    v = Vector([0.0, 1.0])
    printer.title("Orthogonal Vectors (Expected cos = 0)")
    printer.info(f"cos(u, v): {angle_cos(u, v)}")

    # Cas 3 ➔ Vecteurs opposés
    u = Vector([-1.0, 1.0])
    v = Vector([1.0, -1.0])
    printer.title("Opposite Direction (Expected cos = -1)")
    printer.info(f"cos(u, v): {angle_cos(u, v)}")

    # Cas 4 ➔ Colinear, positive
    u = Vector([2.0, 1.0])
    v = Vector([4.0, 2.0])
    printer.title("Colinear Vectors (Expected cos = 1)")
    printer.info(f"cos(u, v): {angle_cos(u, v)}")

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
