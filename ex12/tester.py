from ex12.inverse import inverse
from ex00.matrix import Matrix
from printer import Printer


def main():
    printer = Printer()
    printer.header("DEMO - Ex12: Inverse Matrix")

    # ➤ Matrice inversible 2x2
    printer.title("Inverse of 2x2 Matrix")
    m = Matrix([[4, 7], [2, 6]])
    inv_m = inverse(m)
    printer.print_matrix(inv_m, label="Inverse(m)")

    # ➤ Matrice singulière ➤ devrait lever une erreur
    printer.title("Singular Matrix (should raise an error)")
    try:
        m_sing = Matrix([[1, 2], [2, 4]])
        inverse(m_sing)
    except ValueError as e:
        printer.error(str(e))

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
