import unittest
from ex13.matrix import Matrix
from colorama import Fore, Style


class TestMatrixRank(unittest.TestCase):

    def print_test(self, test_name, operation, expected, obtained):
        """Affichage amélioré des tests."""
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} {operation}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

        if expected == obtained:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_rank(self):
        """Test du calcul du rang d'une matrice."""
        cases = [
            # Matrices carrées classiques
            (Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3),
            (Matrix([[1, 2, 0, 0], [2, 4, 0, 0], [-1, 2, 1, 1]]), 2),
            (Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1], [21, 18, 7]]), 3),
            (Matrix([[1, 2], [2, 4]]), 1),
            (Matrix([[0, 0], [0, 0]]), 0),
            (Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 2),

            (Matrix([[1e10, 2e10, 3e10],
                     [2e10, 4e10, 6e10],
                     [3e10, 6e10, 9e10]]), 1),

            (Matrix([[1 if i == j else 0 for j in range(5)]
                     for i in range(5)]), 5),

            (Matrix([[1, 2, 3], [0, 4, 5], [0, 0, 6]]), 3),
            (Matrix([[1, 0, 0], [2, 3, 0], [3, 4, 5]]), 3),

            # Matrice creuse (avec une seule ligne non nulle)
            (Matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 1),

            # Matrice avec une ligne en double
            (Matrix([[1, 2, 3], [1, 2, 3], [4, 5, 6]]), 2),

            # Matrice avec des valeurs très petites
            (Matrix([[1e-10, 2e-10], [2e-10, 4e-10]]), 1)
        ]

        for matrix, expected in cases:
            result = matrix.rank()
            self.print_test("Calcul du rang",
                            f"{matrix}.rank()", expected, result)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=1)
