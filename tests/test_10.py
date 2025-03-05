import unittest
from ex10.matrix import Matrix
from colorama import Fore, Style


class TestMatrixRowEchelon(unittest.TestCase):

    def matrices_almost_equal(self, mat1, mat2, tol=1e-6):
        if len(mat1) != len(mat2):
            return False
        for row1, row2 in zip(mat1, mat2):
            if len(row1) != len(row2):
                return False
            for a, b in zip(row1, row2):
                if abs(a - b) > tol:
                    return False
        return True

    def print_test(self, test_name, operation, expected, obtained):
        ok = self.matrices_almost_equal(expected, obtained)
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} {operation}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")
        if ok:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_row_echelon(self):
        """Test du calcul de la forme échelonnée par lignes d'une matrice."""
        cases = [
            (Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
             [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
            (Matrix([[1, 2], [3, 4]]),
             [[1, 1.3333333333333333], [0, 1]]),
            (Matrix([[1, 2], [2, 4]]),
             [[1, 2], [0, 0]]),
            (Matrix([[8, 5, -2, 4, 28],
                     [4, 2.5, 20, 4, -4],
                     [8, 5, 1, 4, 17]]),
             [[1.0, 0.625, 0.0, 0.0, -12.1666667],
              [0.0, 0.0, 1.0, 0.0, -3.6666667],
              [0.0, 0.0, 0.0, 1.0, 29.5]])
        ]

        for matrix, expected in cases:
            result = matrix.row_echelon().values
            self.print_test(
                "Forme échelonnée par lignes",
                f"{matrix}.row_echelon()",
                expected,
                result
            )
            for row_res, row_exp in zip(result, expected):
                for val_res, val_exp in zip(row_res, row_exp):
                    self.assertAlmostEqual(val_res, val_exp, places=6)

    def test_row_echelon_singular_matrix(self):
        """Test d'une matrice singulière qui doit rester sous forme
        échelonnée."""
        mat = Matrix([[2, 4, 6],
                      [4, 8, 12],
                      [1, 2, 3]])
        expected = [[1, 2, 3], [0, 0, 0], [0, 0, 0]]
        result = mat.row_echelon().values
        self.print_test("Matrice singulière",
                        "Matrix([[2, 4, 6], [4, 8, 12], [1, 2, 3]])"
                        ".row_echelon()",
                        expected, result)

        self.assertEqual(result, expected)

    def test_row_echelon_zero_matrix(self):
        """Test d'une matrice nulle."""
        mat = Matrix([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]])
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        result = mat.row_echelon().values
        self.print_test("Matrice nulle",
                        "Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])"
                        ".row_echelon()",
                        expected, result)
        self.assertEqual(result, expected)

    def test_row_echelon_identity_matrix(self):
        """Test de la matrice identité."""
        mat = Matrix([[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]])
        expected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        result = mat.row_echelon().values
        self.print_test("Matrice identité",
                        "Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])"
                        ".row_echelon()",
                        expected, result)
        self.assertEqual(result, expected)

    def test_single_row_matrix(self):
        """Test d'une matrice à une seule ligne."""
        mat = Matrix([[2, 4, 6]])
        expected = [[1.0, 2.0, 3.0]]
        result = mat.row_echelon().values
        self.print_test("Matrice à une seule ligne",
                        "Matrix([[2,4,6]]).row_echelon()", expected, result)
        for row_res, row_exp in zip(result, expected):
            for val_res, val_exp in zip(row_res, row_exp):
                self.assertAlmostEqual(val_res, val_exp, places=6)

    def test_single_column_matrix(self):
        """Test d'une matrice à une seule colonne."""
        mat = Matrix([[2], [4], [6]])
        expected = [[1.0], [0.0], [0.0]]
        result = mat.row_echelon().values
        self.print_test("Matrice à une seule colonne",
                        "Matrix([[2],[4],[6]]).row_echelon()",
                        expected, result)
        for row_res, row_exp in zip(result, expected):
            for val_res, val_exp in zip(row_res, row_exp):
                self.assertAlmostEqual(val_res, val_exp, places=6)

    def test_negative_values(self):
        """Test d'une matrice avec des valeurs négatives."""
        mat = Matrix([[-2, -4],
                      [-6, -8]])
        expected = [[1.0, 1.3333333333333333], [0.0, 1.0]]
        result = mat.row_echelon().values
        self.print_test("Matrice avec valeurs négatives",
                        "Matrix([[-2,-4],[-6,-8]]).row_echelon()",
                        expected, result)
        for row_res, row_exp in zip(result, expected):
            for val_res, val_exp in zip(row_res, row_exp):
                self.assertAlmostEqual(val_res, val_exp, places=6)

    def test_rectangular_matrix_more_rows(self):
        """Test d'une matrice rectangulaire
        avec plus de lignes que de colonnes.
        Ici, pour obtenir la RREF sur une matrice non carrée,
        on applique l'élimination vers le haut.
        """
        mat = Matrix([[1, 2],
                      [3, 4],
                      [5, 6],
                      [7, 8]])
        expected = [[1.0, 0.0],
                    [0.0, 1.0],
                    [0.0, 0.0],
                    [0.0, 0.0]]
        result = mat.row_echelon().values
        self.print_test("Matrice rectangulaire (4x2)",
                        "Matrix([[1,2],[3,4],[5,6],[7,8]]).row_echelon()",
                        expected, result)
        for row_res, row_exp in zip(result, expected):
            for val_res, val_exp in zip(row_res, row_exp):
                self.assertAlmostEqual(val_res, val_exp, places=6)

    def test_already_echelon(self):
        """Test d'une matrice déjà en forme échelonnée
        (mais non normalisée sur les lignes non pivots).
        """
        mat = Matrix([[1, 2, 3],
                      [0, 4, 5],
                      [0, 0, 6]])
        expected = [[1.0, 2.0, 3.0],
                    [0.0, 1.0, 1.25],
                    [0.0, 0.0, 1.0]]
        result = mat.row_echelon().values
        self.print_test("Matrice déjà échelonnée",
                        "Matrix([[1,2,3],[0,4,5],[0,0,6]]).row_echelon()",
                        expected, result)
        for row_res, row_exp in zip(result, expected):
            for val_res, val_exp in zip(row_res, row_exp):
                self.assertAlmostEqual(val_res, val_exp, places=6)


if __name__ == "__main__":
    unittest.main(verbosity=1)
