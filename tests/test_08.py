import unittest
from ex08.matrix import Matrix
from colorama import Fore, Style


class TestMatrixTrace(unittest.TestCase):

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

    def test_trace(self):
        """Test du calcul de la trace d'une matrice carrée."""
        cases = [
            (Matrix([[1, 0], [0, 1]]), 2.0),
            (Matrix([[2, -5, 0], [4, 3, 7], [-2, 3, 4]]), 9.0),
            (Matrix([[-2, -8, 4], [1, -23, 4], [0, 6, 4]]), -21.0),
            (Matrix([[10]]), 10.0),
            (Matrix([[0, 0], [0, 0]]), 0.0),
            (Matrix([[1e10, 0], [0, 1e10]]), 2e10),
            (Matrix([[1.5, 0], [0, 2.5]]), 4.0),
            (Matrix([[1e-10, 0], [0, 1e-10]]), 2e-10),
        ]

        for mat, expected in cases:
            result = mat.trace()
            self.print_test("Trace de la matrice",
                            f"{mat}.trace()", expected, result)
            self.assertAlmostEqual(result, expected, places=6)

    def test_trace_errors(self):
        """Test des erreurs levées pour des matrices non carrées."""
        with self.assertRaises(ValueError):
            Matrix([[1, 2, 3], [4, 5, 6]]).trace()


if __name__ == "__main__":
    unittest.main(verbosity=1)
