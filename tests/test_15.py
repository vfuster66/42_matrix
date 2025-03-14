from ex15.complex import Complex
from ex15.vector import Vector
from ex15.matrix import Matrix
from printer import Printer


class TestComplexVectorSpacesColor:

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
        print(f"\nTest: {test_name}")
        print(f"Opération : {operation}")
        print(f"Résultat attendu :\n{expected}")
        print(f"Résultat obtenu  :\n{obtained}")
        if isinstance(expected, Matrix):
            ok = self.matrices_almost_equal(expected, obtained)
        elif isinstance(expected, Vector):
            ok = self.vectors_almost_equal(expected, obtained)
        elif isinstance(expected, Complex):
            ok = self.complex_almost_equal(expected, obtained)
        else:
            ok = expected == obtained

        if ok:
            print("\033[92m✅ Test OK !\033[0m")
        else:
            print("\033[91m❌ Test ÉCHOUÉ !\033[0m")
        print("-" * 50)

    def test_vector_addition(self):
        printer = Printer()
        v1 = Vector([Complex(1, 2), Complex(3, 4)])
        v2 = Vector([Complex(5, -1), Complex(-2, 3)])
        result = v1 + v2
        expected = Vector([Complex(6, 1), Complex(1, 7)])

        self.print_test("Addition de vecteurs", "v1 + v2", expected, result)
        printer.success("✅ Addition de vecteurs réussie !")

    def test_vector_subtraction(self):
        printer = Printer()
        v1 = Vector([Complex(4, 5), Complex(7, 8)])
        v2 = Vector([Complex(1, 2), Complex(3, 4)])
        result = v1 - v2
        expected = Vector([Complex(3, 3), Complex(4, 4)])

        self.print_test(
            "Soustraction de vecteurs", "v1 - v2", expected, result
        )
        printer.success("✅ Soustraction de vecteurs réussie !")

    def test_scalar_multiplication(self):
        printer = Printer()
        v = Vector([Complex(1, 1), Complex(2, -3)])
        scalar = Complex(2, 0)
        result = v.mul_scalar(scalar)
        expected = Vector([Complex(2, 2), Complex(4, -6)])

        self.print_test(
            "Multiplication scalaire", "v.mul_scalar(2)", expected, result
        )
        printer.success("✅ Multiplication scalaire réussie !")

    def test_dot_product(self):
        printer = Printer()
        # Produit scalaire défini comme: somme(x * conjugate(y))
        v1 = Vector([Complex(1, 2), Complex(3, 4)])
        v2 = Vector([Complex(5, -1), Complex(-2, 3)])
        result = v1.dot(v2)
        expected = Complex(9, -6)

        self.print_test("Produit scalaire", "v1.dot(v2)", expected, result)
        printer.success("✅ Produit scalaire réussi !")

    def test_matrix_multiplication(self):
        printer = Printer()
        m1 = Matrix([
            [Complex(1, 2), Complex(3, 4)],
            [Complex(5, 6), Complex(7, 8)]
        ])

        m2 = Matrix([
            [Complex(2, 0), Complex(0, 2)],
            [Complex(1, -1), Complex(-1, -1)]
        ])

        result = m1.mul_mat(m2)

        expected = Matrix([
            [Complex(9, 5), Complex(-3, -5)],
            [Complex(25, 13), Complex(-11, -5)]
        ])

        self.print_test(
            "Multiplication matricielle", "m1.mul_mat(m2)", expected, result
        )
        printer.success("✅ Multiplication matricielle réussie !")


if __name__ == '__main__':
    test = TestComplexVectorSpacesColor()
    test.test_vector_addition()
    test.test_vector_subtraction()
    test.test_scalar_multiplication()
    test.test_dot_product()
    test.test_matrix_multiplication()
