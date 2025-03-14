from ex06.cross_product import cross_product
from ex00.vector import Vector
from printer import Printer


def main():
    printer = Printer()
    printer.header("DEMO - Ex06: Cross Product")

    # Cas 1 ➔ Vecteurs unitaires orthogonaux
    u = Vector([1.0, 0.0, 0.0])
    v = Vector([0.0, 1.0, 0.0])

    printer.title("Cross Product of Unit Vectors (i x j = k)")
    result = cross_product(u, v)
    printer.print_vector(result, label="u x v")  # Expected [0.0, 0.0, 1.0]

    # Cas 2 ➔ Inversé (j x i = -k)
    printer.title("Cross Product (j x i = -k)")
    result = cross_product(v, u)
    printer.print_vector(result, label="v x u")  # Expected [0.0, 0.0, -1.0]

    # Cas 3 ➔ Vecteurs parallèles (produit nul)
    u = Vector([1.0, 2.0, 3.0])
    v = Vector([2.0, 4.0, 6.0])

    printer.title("Parallel Vectors (Cross Product is zero vector)")
    result = cross_product(u, v)
    printer.print_vector(result, label="u x v")  # Expected [0.0, 0.0, 0.0]

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
