import unittest
from ex05.vector import Vector
from ex05.cosine import angle_cos
from colorama import Fore, Style


class TestVectorCosine(unittest.TestCase):

    def print_test(self, test_name, operation, expected, obtained):
        """Affichage amélioré du test avec mise en forme colorée."""
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} {operation}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} "
              f"{round(expected, 6)}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} "
              f"{round(obtained, 6)}")

        if round(expected, 6) == round(obtained, 6):
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_cosine(self):
        """Test du cosinus de l'angle entre deux vecteurs."""
        cases = [
            (Vector([1.0, 0.0]), Vector([1.0, 0.0]), 1.0),
            (Vector([1.0, 0.0]), Vector([0.0, 1.0]), 0.0),
            (Vector([-1.0, 1.0]), Vector([1.0, -1.0]), -1.0),
            (Vector([2.0, 1.0]), Vector([4.0, 2.0]), 1.0),
            (Vector([1.0, 2.0, 3.0]), Vector([4.0, 5.0, 6.0]), 0.974631846),
            (Vector([3.0, -2.0]), Vector([-6.0, 4.0]), -1.0),
            (Vector([1.0, 1.0, 1.0, 1.0]), Vector([2.0, 2.0, 2.0, 2.0]), 1.0),
            (Vector([1e-5, 1e-5]), Vector([1e5, 1e5]), 1.0),
        ]

        for u, v, expected in cases:
            result = angle_cos(u, v)
            self.print_test(
                "Cosinus de l'angle", f"angle_cos({u}, {v})", expected, result
            )
            self.assertAlmostEqual(result, expected, places=6)

    def test_cosine_errors(self):
        """Test des erreurs levées par la fonction."""
        with self.assertRaises(ValueError):
            angle_cos(Vector([1.0, 0.0]), Vector([1.0]))

        with self.assertRaises(ValueError):
            angle_cos(Vector([0.0, 0.0]), Vector([1.0, 1.0]))

        with self.assertRaises(ValueError):
            angle_cos(Vector([1.0, 1.0]), Vector([0.0, 0.0]))


if __name__ == "__main__":
    unittest.main(verbosity=1)
