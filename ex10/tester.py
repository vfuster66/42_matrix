from ex10.row_echelon import row_echelon
from ex00.matrix import Matrix
from printer import Printer


def main():
    printer = Printer()
    printer.header("DEMO - Ex10: Row Echelon Form")

    # ➤ Exemple simple
    printer.title("Matrix ➔ Row Echelon Form")
    m = Matrix([
        [1, 2, -1, -4],
        [2, 3, -1, -11],
        [-2, 0, -3, 22]
    ])

    result = row_echelon(m)
    printer.print_matrix(result, label="Row Echelon Form")

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
