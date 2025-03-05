import unittest
import math
from ex14.matrix import Matrix
from colorama import Fore, Style


class TestMatrixProjection(unittest.TestCase):

    def matrices_almost_equal(self, mat1, mat2, tol=1e-5):
        """Compare deux matrices en vérifiant si
        chaque élément est proche avec une tolérance."""
        for row1, row2 in zip(mat1, mat2):
            for a, b in zip(row1, row2):
                if abs(a - b) > tol:
                    return False
        return True

    def print_test(self, test_name, operation, expected, obtained):
        """Affichage détaillé des tests."""
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} {operation}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL}\n{expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL}\n{obtained}")

        if self.matrices_almost_equal(expected.values, obtained.values):
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_projection_matrix(self):
        """Test de la matrice de projection standard."""

        fov = math.radians(90)
        ratio = 16/9
        near = 0.1
        far = 100.0

        expected = Matrix([
            [1.0 / (math.tan(fov / 2) * ratio), 0, 0, 0],
            [0, 1.0 / math.tan(fov / 2), 0, 0],
            [0, 0, (far + near) / (near - far),
             (2 * far * near) / (near - far)],
            [0, 0, -1, 0]
        ])

        result = Matrix.projection(fov, ratio, near, far)

        self.print_test(
            "Matrice de projection", "Matrix.projection()", expected, result
        )
        self.assertTrue(
            self.matrices_almost_equal(expected.values, result.values)
        )


if __name__ == "__main__":
    unittest.main(verbosity=1)
