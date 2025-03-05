import unittest
from ex07.matrix import Matrix
from ex07.vector import Vector
from colorama import Fore, Style


class TestMatrixOperations(unittest.TestCase):

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

    def test_mul_vec(self):
        """Test de la multiplication matrice-vecteur."""
        cases = [
            (Matrix([[1, 0], [0, 1]]), Vector([4, 2]), Vector([4, 2])),
            (Matrix([[2, 0], [0, 2]]), Vector([4, 2]), Vector([8, 4])),
            (Matrix([[2, -2], [-2, 2]]), Vector([4, 2]), Vector([4, -4])),
        ]

        for mat, vec, expected in cases:
            result = mat.mul_vec(vec)
            self.print_test(
                "Multiplication Matrice-Vecteur",
                f"{mat}.mul_vec({vec})",
                expected.values,
                result.values
            )
            self.assertEqual(result.values, expected.values)

    def test_mul_mat(self):
        """Test de la multiplication matrice-matrice."""
        cases = [
            (Matrix([[1, 0], [0, 1]]),
             Matrix([[1, 0], [0, 1]]),
             Matrix([[1, 0], [0, 1]])),
            (Matrix([[1, 0], [0, 1]]),
             Matrix([[2, 1], [4, 2]]),
             Matrix([[2, 1], [4, 2]])),
            (Matrix([[3, -5], [6, 8]]),
             Matrix([[2, 1], [4, 2]]),
             Matrix([[-14, -7], [44, 22]])),
        ]

        for mat1, mat2, expected in cases:
            result = mat1.mul_mat(mat2)
            self.print_test(
                "Multiplication Matrice-Matrice",
                f"{mat1}.mul_mat({mat2})",
                expected.values,
                result.values
            )
            self.assertEqual(result.values, expected.values)

    def test_mul_vec_errors(self):
        """Test des erreurs pour la multiplication matrice-vecteur."""
        with self.assertRaises(ValueError):
            Matrix([[1, 0], [0, 1]]).mul_vec(Vector([4, 2, 1]))

    def test_mul_mat_errors(self):
        """Test des erreurs pour la multiplication matrice-matrice."""
        with self.assertRaises(ValueError):
            Matrix([[1, 0], [0, 1]]).mul_mat(Matrix([[2, 1]]))


if __name__ == "__main__":
    unittest.main(verbosity=1)
