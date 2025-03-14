from ex08.trace import trace
from ex00.matrix import Matrix
from printer import Printer


def main():
    printer = Printer()
    printer.header("DEMO - Ex08: Trace of a Matrix")

    # Matrice carrée 3x3
    printer.title("Trace of 3x3 Matrix")
    m = Matrix([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]
    ])

    result = trace(m)
    printer.info(f"Trace: {result}")  # Expected 1.0 + 5.0 + 9.0 = 15.0

    # Matrice non carrée ➔ Exception
    printer.title("Non Square Matrix (should raise an error)")
    try:
        m = Matrix([
            [1.0, 2.0],
            [3.0, 4.0],
            [5.0, 6.0]
        ])
        result = trace(m)
        printer.info(f"Trace: {result}")
    except ValueError as e:
        printer.error(str(e))

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
