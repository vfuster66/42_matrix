import unittest
from ex09.matrix import Matrix
from colorama import Fore, Style


class TestMatrixTranspose(unittest.TestCase):

    def print_test(self, test_name, operation, expected, obtained):
        """Affichage amélioré du test avec colorama."""
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} {operation}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

        if expected == obtained:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_transpose(self):
        """Test du calcul de la transposée d'une matrice."""
        cases = [
            (Matrix([[1, 2], [3, 4]]), [[1, 3], [2, 4]]),
            (Matrix([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]]),
            (Matrix([[1, 2, 3]]), [[1], [2], [3]]),
            (Matrix([[1], [2], [3]]), [[1, 2, 3]]),
            (Matrix([[0, 0], [0, 0]]), [[0, 0], [0, 0]]),
            (Matrix([[1, -2], [-3, 4]]), [[1, -3], [-2, 4]]),
        ]

        for matrix, expected in cases:
            result = matrix.transpose().values
            self.print_test(
                "Transposée de la matrice",
                f"{matrix}.transpose()",
                expected,
                result
            )
            self.assertEqual(result, expected)

    def test_transpose_empty_matrix(self):
        """Test de la transposée d'une matrice vide."""
        mat = Matrix([])
        expected = []
        result = mat.transpose().values
        self.print_test(
            "Transposée d'une matrice vide",
            "Matrix([]).transpose()",
            expected,
            result
        )
        self.assertEqual(result, expected)

    def test_transpose_large_matrix(self):
        """Test de la transposée d'une grande matrice (5x5)."""
        mat = Matrix([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ])
        expected = [
            [1, 6, 11, 16, 21],
            [2, 7, 12, 17, 22],
            [3, 8, 13, 18, 23],
            [4, 9, 14, 19, 24],
            [5, 10, 15, 20, 25],
        ]
        result = mat.transpose().values
        self.print_test(
            "Transposée d'une grande matrice (5x5)",
            "Matrix(5x5).transpose()",
            expected,
            result
        )
        self.assertEqual(result, expected)

    def test_transpose_floats(self):
        """Test de la transposée d'une matrice contenant des nombres
        flottants."""
        mat = Matrix([[1.5, 2.5], [3.5, 4.5]])
        expected = [[1.5, 3.5], [2.5, 4.5]]
        result = mat.transpose().values
        self.print_test(
            "Transposée avec des flottants",
            "Matrix([[1.5, 2.5], [3.5, 4.5]]).transpose()",
            expected,
            result
        )
        self.assertEqual(result, expected)

    def test_transpose_extreme_values(self):
        """Test de la transposée d'une matrice contenant des valeurs
        extrêmes."""
        mat = Matrix([[1e10, -1e10], [-1e-10, 1e-10]])
        expected = [[1e10, -1e-10], [-1e10, 1e-10]]
        result = mat.transpose().values
        self.print_test(
            "Transposée avec valeurs extrêmes",
            "Matrix(avec valeurs extrêmes).transpose()",
            expected,
            result
        )
        self.assertEqual(result, expected)

    def test_transpose_single_row_empty(self):
        """Test d'une matrice avec une seule ligne vide."""
        mat = Matrix([[]])
        expected = []
        result = mat.transpose().values
        self.print_test(
            "Transposée d'une matrice avec une seule ligne vide",
            "Matrix([[]]).transpose()",
            expected,
            result
        )
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=1)
