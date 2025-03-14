from ex15.complex import Complex
from ex15.vector import Vector
from printer import Printer


def sqrt_approx(x, epsilon=1e-10):
    """Approximation de la racine carrée par méthode de Newton-Raphson."""
    if x < 0:
        raise ValueError("Cannot compute sqrt of negative number.")
    if x == 0:
        return 0
    guess = x
    while True:
        next_guess = 0.5 * (guess + x / guess)
        if abs(next_guess - guess) < epsilon:
            return next_guess
        guess = next_guess


def main():
    printer = Printer()
    printer.header("DEMO - Ex15: Complex Vector Spaces")

    # ➤ Exemple d'un vecteur complexe
    v = Vector([Complex(1, 2), Complex(3, -4)])  # Utiliser un objet Vector

    # ➤ Affichage du vecteur original
    printer.title("Original Vector")
    printer.print_vector(v)  # Affichage de l'objet Vector

    # ➤ Conjugaison
    conj_v = v.conjugate()  # Applique conjugate() sur le vecteur
    printer.title("Conjugate Vector")
    printer.print_vector(conj_v)

    # ➤ Produit hermitien avec lui-même
    herm_dot = v.dot(v)
    printer.info(f"Hermitian Dot <v|v>: {herm_dot}")

    # ➤ Norme complexe
    norm = v.norm()
    printer.info(f"Complex Norm ||v||: {norm}")

    # ➤ Test de sqrt_approx
    sqrt_val = sqrt_approx(25)
    printer.info(f"Sqrt Approx of 25: {sqrt_val}")

    printer.footer("End of Demo")


if __name__ == "__main__":
    main()
