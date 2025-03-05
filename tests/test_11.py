import unittest
from ex11.matrix import Matrix
from colorama import Fore, Style


class TestMatrixDeterminant(unittest.TestCase):

    def print_test(self, test_name, operation, expected, obtained):
        """Affichage coloré des tests."""
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} {operation}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

        if abs(expected - obtained) < 1e-6:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_determinant_1x1(self):
        """Test du déterminant d'une matrice 1×1."""
        mat = Matrix([[5]])
        expected = 5.0
        result = mat.determinant()
        self.print_test(
            "Déterminant 1×1", "Matrix([[5]]).determinant()", expected, result
        )
        self.assertAlmostEqual(result, expected, places=6)

    def test_determinant_2x2(self):
        """Test du déterminant d'une matrice 2×2."""
        mat = Matrix([[1, -1], [-1, 1]])
        expected = 0.0
        result = mat.determinant()
        self.print_test(
            "Déterminant 2×2",
            "Matrix([[1, -1], [-1, 1]]).determinant()",
            expected,
            result
        )
        self.assertAlmostEqual(result, expected, places=6)

    def test_determinant_3x3(self):
        """Test du déterminant d'une matrice 3×3."""
        mat = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])
        expected = -174.0
        result = mat.determinant()
        self.print_test(
            "Déterminant 3×3",
            "Matrix([[8,5,-2],[4,7,20],[7,6,1]]).determinant()",
            expected,
            result
        )
        self.assertAlmostEqual(result, expected, places=6)

    def test_determinant_4x4(self):
        """Test du déterminant d'une matrice 4×4."""
        mat = Matrix([
            [8, 5, -2, 4],
            [4, 2.5, 20, 4],
            [8, 5, 1, 4],
            [28, -4, 17, 1]
        ])
        expected = 1032.0
        result = mat.determinant()
        self.print_test(
            "Déterminant 4×4",
            "Matrix([...]).determinant()",
            expected,
            result
        )
        self.assertAlmostEqual(result, expected, places=6)

    def test_singular_matrix(self):
        """Test du déterminant d'une matrice singulière (0)."""
        mat = Matrix([[2, 4, 6], [4, 8, 12], [1, 2, 3]])
        expected = 0.0
        result = mat.determinant()
        self.print_test(
            "Matrice singulière",
            "Matrix([[2,4,6],[4,8,12],[1,2,3]]).determinant()",
            expected,
            result
        )
        self.assertAlmostEqual(result, expected, places=6)

    def test_determinant_invalid_size(self):
        """Test d'une matrice non carrée (doit lever une erreur)."""
        with self.assertRaises(ValueError):
            Matrix([[1, 2, 3], [4, 5, 6]]).determinant()

    def test_identity_matrix(self):
        """Test du déterminant d'une matrice identité."""
        for size in range(1, 5):
            mat = Matrix([
                [1 if i == j else 0 for j in range(size)]
                for i in range(size)
            ])
            expected = 1.0
            result = mat.determinant()
            self.print_test(f"Matrice identité {size}x{size}",
                            f"Matrix(Identity {size}x{size}).determinant()",
                            expected, result)
            self.assertAlmostEqual(result, expected, places=6)

    def test_large_numbers(self):
        """Test du déterminant d'une matrice avec des nombres très grands."""
        mat = Matrix([[1e10, 2e10], [3e10, 4e10]])
        expected = -2e20
        result = mat.determinant()
        self.print_test(
            "Matrice grands nombres",
            "Matrix([[1e10,2e10],[3e10,4e10]]).determinant()",
            expected,
            result
        )
        self.assertAlmostEqual(result, expected, places=6)

    def test_small_numbers(self):
        """Test du déterminant d'une matrice avec des nombres très petits."""
        mat = Matrix([[1e-10, 2e-10], [3e-10, 4e-10]])
        expected = -2e-20
        result = mat.determinant()
        self.print_test(
            "Matrice petits nombres",
            "Matrix([[1e-10,2e-10],[3e-10,4e-10]]).determinant()",
            expected,
            result
        )
        self.assertAlmostEqual(result, expected, places=6)

    def test_triangular_matrix(self):
        """Test du déterminant d'une matrice triangulaire supérieure
        et inférieure."""
        upper = Matrix([[2, 3, 1], [0, 5, 4], [0, 0, 7]])
        lower = Matrix([[2, 0, 0], [3, 5, 0], [1, 4, 7]])
        expected = 70.0

        for name, mat in [("Supérieure", upper), ("Inférieure", lower)]:
            result = mat.determinant()
            self.print_test(f"Matrice triangulaire {name}",
                            f"Matrix(triangular {name}).determinant()",
                            expected, result)
            self.assertAlmostEqual(result, expected, places=6)

    def test_zero_row_or_column(self):
        """Test du déterminant d'une matrice ayant une ligne
        ou une colonne remplie de zéros."""
        row_zero = Matrix([[1, 2, 3], [0, 0, 0], [7, 8, 9]])
        col_zero = Matrix([[1, 0, 3], [4, 0, 6], [7, 0, 9]])
        expected = 0.0

        for name, mat in [("Ligne 0", row_zero), ("Colonne 0", col_zero)]:
            result = mat.determinant()
            self.print_test(f"Matrice avec {name} remplie de zéros",
                            f"Matrix({name}).determinant()", expected, result)
            self.assertAlmostEqual(result, expected, places=6)


if __name__ == "__main__":
    unittest.main(verbosity=1)
