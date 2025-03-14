from ex13.projection import projection_matrix
from ex00.vector import Vector
from printer import Printer


def main():
    printer = Printer()
    printer.header("DEMO - Ex13: Projection Matrix")

    # ➤ Exemple : Projection sur u = [1, 0]
    printer.title("Projection on Vector [1, 0]")
    u = Vector([1.0, 0.0])
    P = projection_matrix(u)
    printer.print_matrix(P, label="Projection Matrix")

    # ➤ Exemple : Projection sur u = [1, 1]
    printer.title("Projection on Vector [1, 1]")
    u = Vector([1.0, 1.0])
    P = projection_matrix(u)
    printer.print_matrix(P, label="Projection Matrix")

    # ➤ Cas du vecteur nul ➔ erreur
    printer.title("Projection on Zero Vector (error expected)")
    try:
        u = Vector([0.0, 0.0])
        P = projection_matrix(u)
    except ValueError as e:
        printer.error(str(e))

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
