import unittest
from ex00.vector import Vector
from ex00.matrix import Matrix
from colorama import Fore, Style


class TestVectorMatrixOperations(unittest.TestCase):

    def print_test(self, test_name, operation, expected, obtained):
        """ Affichage amélioré du test avec couleurs et détails """
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} {operation}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

        if expected == obtained:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    # ✅ TESTS POUR VECTOR

    def test_vector_add(self):
        u = Vector([2.0, 3.0])
        v = Vector([5.0, 7.0])
        u.add(v)
        expected = [7.0, 10.0]
        self.print_test("Addition de Vecteurs", "u.add(v)", expected, u.values)
        self.assertEqual(u.values, expected)

    def test_vector_add_negative(self):
        u = Vector([-1.0, -2.0])
        v = Vector([5.0, 7.0])
        u.add(v)
        expected = [4.0, 5.0]
        self.print_test(
            "Addition de Vecteurs (nombres négatifs)",
            "u.add(v)",
            expected,
            u.values
        )
        self.assertEqual(u.values, expected)

    def test_vector_add_error(self):
        u = Vector([1.0, 2.0])
        v = Vector([1.0])
        with self.assertRaises(ValueError):
            u.add(v)

    def test_vector_sub(self):
        u = Vector([2.0, 3.0])
        v = Vector([5.0, 7.0])
        u.sub(v)
        expected = [-3.0, -4.0]
        self.print_test(
            "Soustraction de Vecteurs",
            "u.sub(v)",
            expected,
            u.values
        )
        self.assertEqual(u.values, expected)

    def test_vector_sub_error(self):
        u = Vector([1.0, 2.0])
        v = Vector([1.0])
        with self.assertRaises(ValueError):
            u.sub(v)

    def test_vector_scl(self):
        u = Vector([2.0, 3.0])
        u.scl(2.0)
        expected = [4.0, 6.0]
        self.print_test(
            "Multiplication par un Scalaire (Vecteur)",
            "u.scl(2.0)",
            expected,
            u.values
        )
        self.assertEqual(u.values, expected)

    def test_vector_scl_zero(self):
        u = Vector([1.0, -5.0])
        u.scl(0)
        expected = [0.0, 0.0]
        self.print_test(
            "Multiplication par zéro (Vecteur)",
            "u.scl(0)",
            expected,
            u.values
        )
        self.assertEqual(u.values, expected)

    # ✅ TESTS POUR MATRIX

    def test_matrix_add(self):
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
        u.add(v)
        expected = [[8.0, 6.0], [1.0, 6.0]]
        self.print_test("Addition de Matrices", "u.add(v)", expected, u.values)
        self.assertEqual(u.values, expected)

    def test_matrix_add_error(self):
        u = Matrix([[1.0, 2.0]])
        v = Matrix([[1.0, 2.0], [3.0, 4.0]])
        with self.assertRaises(ValueError):
            u.add(v)

    def test_matrix_sub(self):
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
        u.sub(v)
        expected = [[-6.0, -2.0], [5.0, 2.0]]
        self.print_test(
            "Soustraction de Matrices",
            "u.sub(v)",
            expected,
            u.values
        )
        self.assertEqual(u.values, expected)

    def test_matrix_sub_error(self):
        u = Matrix([[1.0, 2.0]])
        v = Matrix([[1.0, 2.0], [3.0, 4.0]])
        with self.assertRaises(ValueError):
            u.sub(v)

    def test_matrix_scl(self):
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        u.scl(2.0)
        expected = [[2.0, 4.0], [6.0, 8.0]]
        self.print_test(
            "Multiplication par un Scalaire (Matrice)",
            "u.scl(2.0)",
            expected,
            u.values
        )
        self.assertEqual(u.values, expected)

    def test_matrix_scl_zero(self):
        u = Matrix([[1.0, -5.0], [2.0, 3.0]])
        u.scl(0)
        expected = [[0.0, 0.0], [0.0, 0.0]]
        self.print_test(
            "Multiplication par zéro (Matrice)",
            "u.scl(0)",
            expected,
            u.values
        )
        self.assertEqual(u.values, expected)


if __name__ == "__main__":
    unittest.main(verbosity=1)
