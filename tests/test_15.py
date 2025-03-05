import unittest
from ex15.complex import Complex
from ex15.vector import Vector
from ex15.matrix import Matrix
from colorama import Fore, Style, init

init(autoreset=True)


class TestComplexVectorSpacesColor(unittest.TestCase):

    def complex_almost_equal(self, a, b, tol=1e-5):
        """Compare deux nombres complexes avec une tolérance."""
        return abs(a.real - b.real) < tol and abs(a.imag - b.imag) < tol

    def vectors_almost_equal(self, vec1, vec2, tol=1e-5):
        """Compare deux vecteurs de nombres complexes avec une tolérance."""
        if len(vec1.values) != len(vec2.values):
            return False
        for a, b in zip(vec1.values, vec2.values):
            if not self.complex_almost_equal(a, b, tol):
                return False
        return True

    def matrices_almost_equal(self, mat1, mat2, tol=1e-5):
        """Compare deux matrices de nombres complexes avec une tolérance."""
        if len(mat1.values) != len(mat2.values):
            return False
        for row1, row2 in zip(mat1.values, mat2.values):
            if len(row1) != len(row2):
                return False
            for a, b in zip(row1, row2):
                if not self.complex_almost_equal(a, b, tol):
                    return False
        return True

    def print_test(self, test_name, operation, expected, obtained):
        """Affichage détaillé du test avec colorama."""
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} {operation}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL}\n{expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL}\n{obtained}")
        # Détermination du type pour la comparaison
        if isinstance(expected, Matrix):
            ok = self.matrices_almost_equal(expected, obtained)
        elif isinstance(expected, Vector):
            ok = self.vectors_almost_equal(expected, obtained)
        elif isinstance(expected, Complex):
            ok = self.complex_almost_equal(expected, obtained)
        else:
            ok = expected == obtained

        if ok:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_vector_addition(self):
        v1 = Vector([Complex(1, 2), Complex(3, 4)])
        v2 = Vector([Complex(5, -1), Complex(-2, 3)])
        result = v1 + v2
        expected = Vector([Complex(6, 1), Complex(1, 7)])
        self.print_test("Addition de vecteurs", "v1 + v2", expected, result)
        self.assertTrue(self.vectors_almost_equal(result, expected))

    def test_vector_subtraction(self):
        v1 = Vector([Complex(4, 5), Complex(7, 8)])
        v2 = Vector([Complex(1, 2), Complex(3, 4)])
        result = v1 - v2
        expected = Vector([Complex(3, 3), Complex(4, 4)])
        self.print_test("Soustraction de vecteurs",
                        "v1 - v2", expected, result)
        self.assertTrue(self.vectors_almost_equal(result, expected))

    def test_scalar_multiplication(self):
        v = Vector([Complex(1, 1), Complex(2, -3)])
        scalar = Complex(2, 0)
        result = v.mul_scalar(scalar)
        expected = Vector([Complex(2, 2), Complex(4, -6)])
        self.print_test("Multiplication scalaire",
                        "v.mul_scalar(2)",
                        expected,
                        result)
        self.assertTrue(self.vectors_almost_equal(result, expected))

    def test_dot_product(self):
        # Produit scalaire défini comme: somme(x * conjugate(y))
        v1 = Vector([Complex(1, 2), Complex(3, 4)])
        v2 = Vector([Complex(5, -1), Complex(-2, 3)])
        # Calcul manuel pour vérification :
        # (1+2i)*(5+1i) = 3+11i, (3+4i)*(-2-3i) = 6-17i, somme = 9 - 6i
        result = v1.dot(v2)
        expected = Complex(9, -6)
        self.print_test("Produit scalaire", "v1.dot(v2)", expected, result)
        self.assertTrue(self.complex_almost_equal(result, expected))

    def test_matrix_multiplication(self):
        """Test de la multiplication de matrices complexes."""
        m1 = Matrix([
            [Complex(1, 2), Complex(3, 4)],
            [Complex(5, 6), Complex(7, 8)]
        ])

        m2 = Matrix([
            [Complex(2, 0), Complex(0, 2)],
            [Complex(1, -1), Complex(-1, -1)]
        ])

        result = m1.mul_mat(m2)

        # Matrice attendue (calculée à la main pour vérification)
        expected = Matrix([
            [Complex(9, 5), Complex(-3, -5)],
            [Complex(25, 13), Complex(-11, -5)]
        ])

        self.print_test("Multiplication matricielle",
                        "m1.mul_mat(m2)", expected, result)

        self.assertTrue(self.matrices_almost_equal(result, expected))

    def test_matrix_trace(self):
        m = Matrix([[Complex(1, 1), Complex(2, -1)],
                    [Complex(3, 4), Complex(5, 5)]])
        result = m.trace()
        expected = Complex(6, 6)
        self.print_test("Trace de matrice", "m.trace()", expected, result)
        self.assertTrue(self.complex_almost_equal(result, expected))

    def test_zero_matrix(self):
        """Test de la multiplication avec une matrice nulle."""
        m1 = Matrix([
            [Complex(1, 2), Complex(3, 4)],
            [Complex(5, 6), Complex(7, 8)]
        ])

        zero = Matrix([
            [Complex(0, 0), Complex(0, 0)],
            [Complex(0, 0), Complex(0, 0)]
        ])

        result = m1.mul_mat(zero)
        expected = zero

        self.print_test("Multiplication par matrice nulle",
                        "m1.mul_mat(zero)", expected, result)
        self.assertTrue(self.matrices_almost_equal(result, expected))

    def test_identity_matrix(self):
        """Test de la multiplication avec une matrice identité."""
        identity = Matrix([
            [Complex(1, 0), Complex(0, 0)],
            [Complex(0, 0), Complex(1, 0)]
        ])

        m1 = Matrix([
            [Complex(4, -3), Complex(2, 5)],
            [Complex(-1, 7), Complex(6, -2)]
        ])

        result = m1.mul_mat(identity)
        expected = m1

        self.print_test("Multiplication par identité",
                        "m1.mul_mat(identity)", expected, result)
        self.assertTrue(self.matrices_almost_equal(result, expected))

    def test_large_values(self):
        """Test de la multiplication
        avec des valeurs complexes très grandes."""
        large_matrix = Matrix([
            [Complex(1e6, -1e6), Complex(2e6, 3e6)],
            [Complex(-3e6, 4e6), Complex(5e6, -6e6)]
        ])

        scalar = Complex(1e-6, 0)

        result = large_matrix.mul_scalar(scalar)
        expected = Matrix([
            [Complex(1, -1), Complex(2, 3)],
            [Complex(-3, 4), Complex(5, -6)]
        ])

        self.print_test(
            "Multiplication par grand scalaire",
            "large_matrix.mul_scalar(1e-6)",
            expected,
            result)
        self.assertTrue(self.matrices_almost_equal(result, expected))

    def test_small_values(self):
        """Test de la multiplication
        avec des valeurs complexes très petites."""
        small_matrix = Matrix([
            [Complex(1e-6, -1e-6), Complex(2e-6, 3e-6)],
            [Complex(-3e-6, 4e-6), Complex(5e-6, -6e-6)]
        ])

        scalar = Complex(1e6, 0)

        result = small_matrix.mul_scalar(scalar)
        expected = Matrix([
            [Complex(1, -1), Complex(2, 3)],
            [Complex(-3, 4), Complex(5, -6)]
        ])

        self.print_test(
            "Multiplication par petit scalaire",
            "small_matrix.mul_scalar(1e6)",
            expected,
            result
        )
        self.assertTrue(self.matrices_almost_equal(result, expected))

    def test_addition_commutativity(self):
        """Test de la commutativité de l'addition de matrices complexes."""
        m1 = Matrix([
            [Complex(1, 2), Complex(3, 4)],
            [Complex(5, 6), Complex(7, 8)]
        ])

        m2 = Matrix([
            [Complex(9, -1), Complex(-2, 3)],
            [Complex(4, 2), Complex(0, 5)]
        ])

        result1 = m1 + m2
        result2 = m2 + m1

        self.print_test(
            "Commutativité de l'addition",
            "m1 + m2 == m2 + m1",
            result1,
            result2
        )
        self.assertTrue(self.matrices_almost_equal(result1, result2))

    def test_scalar_distributivity(self):
        """Test de la distributivité de la multiplication scalaire."""
        scalar = Complex(2, 3)

        m1 = Matrix([
            [Complex(1, 2), Complex(3, 4)],
            [Complex(5, 6), Complex(7, 8)]
        ])

        m2 = Matrix([
            [Complex(2, 1), Complex(4, -3)],
            [Complex(6, -5), Complex(8, 0)]
        ])

        result1 = (m1 + m2).mul_scalar(scalar)
        result2 = m1.mul_scalar(scalar) + m2.mul_scalar(scalar)

        self.print_test(
            "Distributivité scalaire",
            "a * (A + B) == a * A + a * B",
            result1,
            result2
        )
        self.assertTrue(self.matrices_almost_equal(result1, result2))

    # 🔹 TESTS SUR L’INVERSE
    def test_inverse_2x2(self):
        """Test de l'inverse d'une matrice 2x2 complexe."""
        m = Matrix([
            [Complex(1, 1), Complex(2, -1)],
            [Complex(3, 4), Complex(5, 5)]
        ])
        inv = m.inverse()
        expected = m.mul_mat(inv)  # Devrait donner l'identité
        identity = Matrix([
            [Complex(1, 0), Complex(0, 0)],
            [Complex(0, 0), Complex(1, 0)]
        ])
        self.print_test("Inverse de matrice 2x2", "m.inverse()",
                        expected, identity)
        self.assertTrue(self.matrices_almost_equal(expected, identity))

    def test_inverse_singular(self):
        """Test d'une matrice singulière qui n'a pas d'inverse."""
        m = Matrix([
            [Complex(1, 2), Complex(2, 4)],
            [Complex(3, 6), Complex(6, 12)]
        ])
        with self.assertRaises(ValueError):
            m.inverse()

    def test_determinant_singular(self):
        """Test d'une matrice dont le déterminant est 0."""
        m = Matrix([
            [Complex(1, 2), Complex(2, 4)],
            [Complex(3, 6), Complex(6, 12)]
        ])
        result = m.determinant()
        expected = Complex(0, 0)
        self.print_test("Déterminant matrice singulière",
                        "m.determinant()", expected, result)
        self.assertTrue(self.complex_almost_equal(result, expected))

    # 🔹 TESTS SUR LE RANG
    def test_rank_full(self):
        """Test du rang d'une matrice pleine."""
        m = Matrix([
            [Complex(1, 1), Complex(2, -1)],
            [Complex(3, 4), Complex(5, 5)]
        ])
        result = m.rank()
        expected = 2
        self.assertEqual(result, expected)

    def test_rank_dependent_rows(self):
        """Test du rang d'une matrice avec des lignes dépendantes."""
        m = Matrix([
            [Complex(1, 2), Complex(2, 4)],
            [Complex(3, 6), Complex(6, 12)]
        ])
        result = m.rank()
        expected = 1
        self.assertEqual(result, expected)

    # 🔹 TESTS SUR LES PROPRIÉTÉS ALGÉBRIQUES
    def test_matrix_multiplication_associativity(self):
        """Test de l'associativité de la multiplication de matrices."""
        A = Matrix([
            [Complex(1, 1), Complex(2, -1)],
            [Complex(3, 4), Complex(5, 5)]
        ])
        B = Matrix([
            [Complex(2, 3), Complex(4, -1)],
            [Complex(1, 0), Complex(5, 2)]
        ])
        C = Matrix([
            [Complex(0, 1), Complex(3, -3)],
            [Complex(2, 2), Complex(1, 1)]
        ])
        result1 = A.mul_mat(B.mul_mat(C))
        result2 = (A.mul_mat(B)).mul_mat(C)
        self.print_test(
            "Associativité multiplication",
            "(A * B) * C == A * (B * C)",
            result1,
            result2
        )
        self.assertTrue(self.matrices_almost_equal(result1, result2))

    def test_matrix_addition_commutativity(self):
        """Test de la commutativité de l'addition."""
        A = Matrix([
            [Complex(1, 1), Complex(2, -1)],
            [Complex(3, 4), Complex(5, 5)]
        ])
        B = Matrix([
            [Complex(2, 3), Complex(4, -1)],
            [Complex(1, 0), Complex(5, 2)]
        ])
        result1 = A + B
        result2 = B + A
        self.print_test("Commutativité de l'addition",
                        "A + B == B + A",
                        result1,
                        result2)
        self.assertTrue(self.matrices_almost_equal(result1, result2))

    def test_matrix_multiplication_identity(self):
        """Test de la multiplication par une matrice identité."""
        A = Matrix([
            [Complex(1, 2), Complex(3, 4)],
            [Complex(5, 6), Complex(7, 8)]
        ])
        identity_matrix = Matrix([
            [Complex(1, 0), Complex(0, 0)],
            [Complex(0, 0), Complex(1, 0)]
        ])
        result = A.mul_mat(identity_matrix)
        self.print_test("Multiplication par identité",
                        "A * identity_matrix",
                        result,
                        A)
        self.assertTrue(self.matrices_almost_equal(result, A))


if __name__ == '__main__':
    unittest.main(verbosity=2)
