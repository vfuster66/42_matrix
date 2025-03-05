import unittest
from ex03.vector import Vector
from colorama import Fore, Style


class TestDotProduct(unittest.TestCase):

    def print_test(self, test_name, operation, expected, obtained):
        """Affichage amélioré du test."""
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} {operation}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

        if expected == obtained:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_dot_product(self):
        cases = [
            (Vector([0.0, 0.0]), Vector([1.0, 1.0]), 0.0),
            (Vector([1.0, 1.0]), Vector([1.0, 1.0]), 2.0),
            (Vector([-1.0, 6.0]), Vector([3.0, 2.0]), 9.0),
            (Vector([1.0, -1.0]), Vector([-1.0, 1.0]), -2.0),
        ]

        for u, v, expected in cases:
            result = u.dot(v)
            self.print_test(
                "Produit Scalaire", f"dot({u}, {v})", expected, result
            )
            self.assertAlmostEqual(result, expected, places=6)

    def test_dot_product_errors(self):
        """Test d'erreur sur des dimensions incompatibles."""
        with self.assertRaises(ValueError):
            Vector([1.0, 2.0]).dot(Vector([1.0]))

    def test_dot_product_extreme_cases(self):
        """Test du produit scalaire avec des nombres extrêmes."""
        cases = [
            (Vector([1e10, 2e10]), Vector([3e10, 4e10]), 1.1e21),
            (Vector([1e-10, 2e-10]), Vector([3e-10, 4e-10]),
             sum([1e-10 * 3e-10, 2e-10 * 4e-10])),
            (Vector([0, 0, 1]), Vector([0, 0, 5]), 5),
            (Vector([-1, -2, 3]), Vector([4, -5, 6]), 24)
        ]

        for u, v, expected in cases:
            result = u.dot(v)
            self.print_test(
                "Produit Scalaire (Cas Extrêmes)",
                f"dot({u}, {v})",
                expected,
                result
            )
            self.assertAlmostEqual(result, expected, places=10)

    def test_dot_product_errors_additional(self):
        """Tests supplémentaires sur les erreurs."""

        with self.assertRaises(ValueError):
            Vector([1.0, 2.0]).dot(Vector([1.0, 2.0, 3.0]))

        with self.assertRaises(TypeError):
            Vector([1.0, None])

        with self.assertRaises(ValueError):
            Vector([float('nan'), 2.0])

        with self.assertRaises(ValueError):
            Vector([]).dot(Vector([]))

    def is_nan(value):
        """
        Détecte si une valeur est NaN sans utiliser de bibliothèque externe.
        """
        return value != value


if __name__ == "__main__":
    unittest.main(verbosity=1)
