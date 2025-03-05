import unittest
from ex06.vector import Vector
from ex06.cross_product import cross_product
from colorama import Fore, Style


class TestCrossProduct(unittest.TestCase):

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

    def test_cross_product(self):
        """Test du produit vectoriel avec plusieurs vecteurs 3D."""
        cases = [
            (Vector([0.0, 0.0, 1.0]), Vector([1.0, 0.0, 0.0]), Vector(
                [0.0, 1.0, 0.0])),
            (Vector([1.0, 2.0, 3.0]), Vector([4.0, 5.0, 6.0]), Vector(
                [-3.0, 6.0, -3.0])),
            (Vector([4.0, 2.0, -3.0]), Vector([-2.0, -5.0, 16.0]), Vector(
                [17.0, -58.0, -16.0])),
            (Vector([1.0, 0.0, 0.0]), Vector([0.0, 1.0, 0.0]), Vector(
                [0.0, 0.0, 1.0])),
            (Vector([0.0, 1.0, 0.0]), Vector([0.0, 0.0, 1.0]), Vector(
                [1.0, 0.0, 0.0])),
            (Vector([0.0, 0.0, 1.0]), Vector([0.0, 1.0, 0.0]), Vector(
                [-1.0, 0.0, 0.0])),
            (Vector([1.0, 2.0, 3.0]), Vector([1.0, 2.0, 3.0]), Vector(
                [0.0, 0.0, 0.0])),
            (Vector([2.0, 4.0, 6.0]), Vector([1.0, 2.0, 3.0]), Vector(
                [0.0, 0.0, 0.0])),
            (Vector([1e10, 2e10, 3e10]), Vector([4e10, 5e10, 6e10]), Vector(
                [-3e20, 6e20, -3e20])),
        ]

        for u, v, expected in cases:
            result = cross_product(u, v)
            self.print_test(
                "Produit vectoriel",
                f"cross_product({u}, {v})",
                expected.values,
                result.values
            )
            for r, e in zip(result.values, expected.values):
                self.assertAlmostEqual(r, e, places=18)

    def test_cross_product_errors(self):
        """Test des erreurs levées pour des vecteurs non 3D."""
        with self.assertRaises(ValueError):
            cross_product(Vector([1.0, 2.0]), Vector([4.0, 5.0]))

        with self.assertRaises(ValueError):
            cross_product(
                Vector([1.0, 2.0, 3.0, 4.0]), Vector([4.0, 5.0, 6.0])
                )


if __name__ == "__main__":
    unittest.main(verbosity=1)
