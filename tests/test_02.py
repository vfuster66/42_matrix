import unittest
from ex02.lerp import lerp
from ex02.vector import Vector
from ex02.matrix import Matrix
from colorama import Fore, Style


class TestLerpFunction(unittest.TestCase):

    def print_test(self, test_name, operation, expected, obtained):
        """Affichage amélioré du test"""
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} {operation}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

        if expected == obtained:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    # ✅ TESTS SUR LES SCALAIRES
    def test_lerp_scalar(self):
        cases = [
            (0.0, 1.0, 0.0, 0.0),
            (0.0, 1.0, 1.0, 1.0),
            (0.0, 1.0, 0.5, 0.5),
            (21.0, 42.0, 0.3, 27.3),
            (-10.0, 10.0, 0.5, 0.0),
            (1000.0, 2000.0, 0.75, 1750.0)
        ]

        for u, v, t, expected in cases:
            result = lerp(u, v, t)
            self.print_test(
                f"Interpolation Scalaire (t={t})",
                f"lerp({u}, {v}, {t})",
                expected,
                result
            )
            self.assertAlmostEqual(result, expected, places=10)

    # ✅ TESTS SUR LES VECTEURS
    def test_lerp_vector(self):
        cases = [
            (Vector([2.0, 1.0]), Vector([4.0, 2.0]), 0.3, Vector([2.6, 1.3])),
            (Vector([-1.0, -2.0]), Vector([5.0, 7.0]), 0.5,
             Vector([2.0, 2.5])),
            (Vector([10.0, 20.0]), Vector([30.0, 40.0]), 1.0,
             Vector([30.0, 40.0]))
        ]

        for u, v, t, expected in cases:
            result = lerp(u, v, t)
            self.print_test(
                "Interpolation Vecteur",
                f"lerp({u}, {v}, {t})",
                expected,
                result
            )

        for i, (res, exp) in enumerate(zip(result.values, expected.values)):
            try:
                self.assertAlmostEqual(res, exp, places=6)
            except AssertionError:
                print(f"Échec sur l'élément {i} du vecteur : {res} != {exp}")
                raise

    # ✅ TESTS SUR LES MATRICES
    def test_lerp_matrix(self):
        cases = [
            (
                Matrix([[2.0, 1.0], [3.0, 4.0]]),
                Matrix([[20.0, 10.0], [30.0, 40.0]]),
                0.5,
                Matrix([[11.0, 5.5], [16.5, 22.0]])
            ),
            (
                Matrix([[0.0, 0.0], [0.0, 0.0]]),
                Matrix([[10.0, 20.0], [30.0, 40.0]]),
                0.2,
                Matrix([[2.0, 4.0], [6.0, 8.0]])
            ),
            (
                Matrix([[-10.0, -20.0], [-30.0, -40.0]]),
                Matrix([[10.0, 20.0], [30.0, 40.0]]),
                0.5,
                Matrix([[0.0, 0.0], [0.0, 0.0]])
            )
        ]

        for u, v, t, expected in cases:
            result = lerp(u, v, t)
            self.print_test(
                "Interpolation Matrice",
                f"lerp({u}, {v}, {t})",
                expected,
                result
            )

        for i, (row_res, row_exp) in enumerate(
            zip(result.values, expected.values)
        ):
            for j, (res, exp) in enumerate(zip(row_res, row_exp)):
                try:
                    self.assertAlmostEqual(res, exp, places=6)
                except AssertionError:
                    print(
                        f"Échec sur l'élément [{i}][{j}] de la matrice : "
                        f"{res} != {exp}"
                    )
                    raise

    # ❌ TESTS D'ERREURS

    def test_lerp_errors(self):
        error_cases = [
            (Vector([1, 2]), Vector([1]), 0.5, ValueError),
            (Matrix([[1, 2]]), Matrix([[1, 2], [3, 4]]), 0.5, ValueError),
            (2.0, Vector([1, 2]), 0.5, TypeError),
            (2.0, 3.0, -0.5, ValueError),
            (Vector([1.0, 2.0]),
             Matrix([[1.0, 2.0], [3.0, 4.0]]),
             0.5,
             TypeError)
        ]

        for u, v, t, expected_exception in error_cases:
            with self.assertRaises(expected_exception):
                lerp(u, v, t)

    def test_lerp_edge_cases(self):
        """Tests des cas extrêmes et des valeurs limites"""

        cases = [
            (0.0, 1.0, 1e-10, 1e-10),
            (0.0, 1.0, 0.9999999999, 0.9999999999)
        ]

        for u, v, t, expected in cases:
            result = lerp(u, v, t)
            self.print_test(
                f"Interpolation Scalaire Extrême (t={t})",
                f"lerp({u}, {v}, {t})",
                expected,
                result
            )
            self.assertAlmostEqual(result, expected, places=10)

        with self.assertRaises(ValueError):
            lerp(float('nan'), 42.0, 0.5)

        with self.assertRaises(ValueError):
            lerp(42.0, float('nan'), 0.5)

        with self.assertRaises(ValueError):
            lerp(42.0, 42.0, float('nan'))


if __name__ == "__main__":
    unittest.main(verbosity=1)
