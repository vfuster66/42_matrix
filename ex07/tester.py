from ex07.matrix_multiplication import matmul
from ex00.matrix import Matrix
from ex00.vector import Vector
from printer import Printer


def main():
    printer = Printer()
    printer.header("DEMO - Ex07: Matrix Multiplication")

    # ➤ Matrice * Vecteur
    printer.title("Matrix * Vector")
    m = Matrix([[1, 2], [3, 4], [5, 6]])
    v = Vector([7, 8])

    result = matmul(m, v)
    printer.print_vector(result, label="m * v")

    # ➤ Matrice * Matrice
    printer.title("Matrix * Matrix")
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    m2 = Matrix([[7, 8], [9, 10], [11, 12]])

    result = matmul(m1, m2)
    printer.print_matrix(result, label="m1 * m2")

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
