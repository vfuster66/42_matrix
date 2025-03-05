import unittest
from ex12.matrix import Matrix
from colorama import Fore, Style


class TestMatrixInverse(unittest.TestCase):

    @staticmethod
    def matrices_almost_equal(mat1, mat2, tol=1e-3):
        """Compare deux matrices en vérifiant
        si chaque élément est proche avec une tolérance."""
        if len(mat1) != len(mat2):
            return False
        for i, (row1, row2) in enumerate(zip(mat1, mat2)):
            if len(row1) != len(row2):
                return False
            for j, (a, b) in enumerate(zip(row1, row2)):
                diff = abs(a - b)
                if diff > tol:
                    print(
                        f"❌ Différence trop grande à ({i}, {j}) : {a} vs {b}, "
                        )
                    print(f"diff={diff}")
                    print(f"diff={diff}")
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

    def test_inverse_identity(self):
        """Test de l'inverse d'une matrice identité."""
        for n in range(1, 5):
            identity = [
                [1 if i == j else 0 for j in range(n)]
                for i in range(n)
            ]
            mat = Matrix(identity)
            expected = identity
            result = mat.inverse().values
            self.print_test(
                f"Matrice identité {n}x{n}",
                f"Matrix(Identity {n}x{n}).inverse()",
                expected,
                result
            )
            self.assertTrue(self.matrices_almost_equal(expected, result))

    def test_inverse_basic(self):
        """Test d'inversion de matrices basiques."""
        cases = [
            (Matrix([[2, 0], [0, 2]]), [[0.5, 0], [0, 0.5]]),
            (Matrix([[4, 7], [2, 6]]), [[0.6, -0.7], [-0.2, 0.4]]),
            (Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]]), [
                [0.649425287, 0.097701149, -0.655172414],
                [-0.781609195, -0.126436782, 0.965517241],
                [0.143678161, 0.074712644, -0.206896552]
            ])
        ]
        for matrix, expected in cases:
            result = matrix.inverse().values
            self.print_test(
                "Inversion de matrice",
                f"{matrix}.inverse()",
                expected,
                result
            )
            self.assertTrue(self.matrices_almost_equal(expected, result))

    def test_inverse_singular(self):
        """Test d'une matrice singulière (det = 0)."""
        mat = Matrix([[2, 4, 6], [4, 8, 12], [1, 2, 3]])
        with self.assertRaises(ValueError):
            mat.inverse()

    def test_inverse_large_numbers(self):
        """Test d'une matrice avec des nombres très grands."""
        mat = Matrix([[1e10, 2e10], [3e10, 4e10]])
        expected = [[-2e-10, 1e-10], [1.5e-10, -0.5e-10]]
        result = mat.inverse().values
        self.print_test(
            "Matrice grands nombres",
            "Matrix([[1e10,2e10],[3e10,4e10]]).inverse()",
            expected,
            result
        )
        self.assertTrue(self.matrices_almost_equal(expected, result))

    def test_inverse_diagonal(self):
        """Test d'une matrice diagonale avec des coefficients variés."""
        mat = Matrix([[3, 0, 0], [0, -2, 0], [0, 0, 0.5]])
        expected = [[1/3, 0, 0], [0, -0.5, 0], [0, 0, 2]]
        result = mat.inverse().values
        self.print_test(
            "Matrice diagonale",
            "Matrix([[3,0,0],[0,-2,0],[0,0,0.5]]).inverse()",
            expected,
            result
        )
        self.assertTrue(self.matrices_almost_equal(expected, result))

    def test_inverse_triangular(self):
        """Test d'une matrice triangulaire (supérieure et inférieure)."""
        upper_triangular = Matrix([[2, 1, -1], [0, 3, 4], [0, 0, 5]])
        expected_upper = [
            [0.5, -1/6, 7/30],
            [0, 1/3, -4/15],
            [0, 0, 0.2]
        ]
        result_upper = upper_triangular.inverse().values
        self.print_test(
            "Matrice triangulaire supérieure",
            "Matrix(triangular Supérieure).inverse()",
            expected_upper,
            result_upper
        )
        self.assertTrue(
            self.matrices_almost_equal(expected_upper, result_upper)
        )

        lower_triangular = Matrix([[2, 0, 0], [1, 3, 0], [-1, 4, 5]])
        expected_lower = [
            [0.5, 0, 0],
            [-1/6, 1/3, 0],
            [7/30, -4/15, 0.2]
        ]
        result_lower = lower_triangular.inverse().values
        self.print_test(
            "Matrice triangulaire inférieure",
            "Matrix(triangular Inférieure).inverse()",
            expected_lower,
            result_lower
        )
        self.assertTrue(
            self.matrices_almost_equal(expected_lower, result_lower)
        )


if __name__ == "__main__":
    unittest.main(verbosity=1)
