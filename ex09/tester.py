from ex09.transpose import transpose
from ex00.matrix import Matrix
from printer import Printer


def main():
    printer = Printer()
    printer.header("DEMO - Ex09: Transpose Matrix")

    # ➤ Transpose 3x2 ➔ 2x3
    m = Matrix([
        [1, 2],
        [3, 4],
        [5, 6]
    ])
    printer.title("Transpose 3x2 Matrix ➔ 2x3")
    result = transpose(m)
    printer.print_matrix(result, label="Transpose(m)")

    # ➤ Transpose square matrix
    m_square = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    printer.title("Transpose 3x3 Matrix")
    result = transpose(m_square)
    printer.print_matrix(result, label="Transpose(m_square)")

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
