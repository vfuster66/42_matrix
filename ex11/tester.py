from ex11.determinant import determinant
from ex00.matrix import Matrix
from printer import Printer


def main():
    printer = Printer()
    printer.header("DEMO - Ex11: Determinant")

    # Matrice 2x2
    printer.title("Determinant of 2x2 Matrix")
    m = Matrix([[4, 6], [3, 8]])
    result = determinant(m)
    printer.info(f"det(m): {result}")  # Expected: 4*8 - 6*3 = 32 - 18 = 14

    # Matrice 3x3
    printer.title("Determinant of 3x3 Matrix")
    m = Matrix([
        [6, 1, 1],
        [4, -2, 5],
        [2, 8, 7]
    ])
    result = determinant(m)
    printer.info(f"det(m): {result}")  # Expected: -306

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
