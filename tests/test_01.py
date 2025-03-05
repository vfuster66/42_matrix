"""
Tests unitaires pour la fonction linear_combination du module ex01.
"""

import unittest
from colorama import Fore, Style
from ex01.vector import Vector
from ex01.linear_combination import linear_combination


class TestLinearCombination(unittest.TestCase):
    """Classe de tests pour la fonction linear_combination."""

    def print_test(self, test_name, operation, expected, obtained):
        """
        Affichage amélioré du test avec couleurs et détails.

        :param test_name: Nom du test.
        :param operation: Description de l'opération testée.
        :param expected: Résultat attendu.
        :param obtained: Résultat obtenu.
        """
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} {operation}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

        if expected == obtained:
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_linear_combination_standard(self):
        """Test d'une combinaison linéaire classique."""
        e1 = Vector([1.0, 0.0, 0.0])
        e2 = Vector([0.0, 1.0, 0.0])
        e3 = Vector([0.0, 0.0, 1.0])

        result = linear_combination([e1, e2, e3], [10.0, -2.0, 0.5])
        expected = Vector([10.0, -2.0, 0.5])

        self.print_test("Combinaison Linéaire Simple",
                        "linear_combination([e1, e2, e3], [10, -2, 0.5])",
                        expected.values, result.values)
        self.assertEqual(result.values, expected.values)

    def test_linear_combination_different_vectors(self):
        """Test avec des vecteurs ayant des valeurs variées."""
        v1 = Vector([1.0, 2.0, 3.0])
        v2 = Vector([0.0, 10.0, -100.0])

        result = linear_combination([v1, v2], [10.0, -2.0])
        expected = Vector([10.0, 0.0, 230.0])

        self.print_test("Combinaison Linéaire Différente",
                        "linear_combination([v1, v2], [10, -2])",
                        expected.values, result.values)
        self.assertEqual(result.values, expected.values)

    def test_linear_combination_empty(self):
        """Test avec une liste vide de vecteurs."""
        result = linear_combination([], [])
        expected = Vector([0])

        self.print_test("Combinaison Linéaire Vide",
                        "linear_combination([], [])",
                        expected.values, result.values)
        self.assertEqual(result.values, expected.values)

    def test_linear_combination_mismatched_lengths(self):
        """Test avec des listes de tailles différentes."""
        e1 = Vector([1.0, 0.0, 0.0])
        e2 = Vector([0.0, 1.0, 0.0])

        with self.assertRaises(ValueError):
            linear_combination([e1, e2], [10.0])

        print(f"\n{Fore.CYAN}Test: Combinaison Linéaire Longueur "
              f"Incorrecte{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} "
              f"linear_combination([e1, e2], [10])")
        print(f"{Fore.RED}⛔ Exception attendue : ValueError{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✅ Test OK ! "
              f"(Exception levée comme prévu){Style.RESET_ALL}")
        print("-" * 50)

    def test_linear_combination_dimension_mismatch(self):
        """Test avec des vecteurs de tailles différentes."""
        v1 = Vector([1.0, 2.0])
        v2 = Vector([1.0, 2.0, 3.0])

        with self.assertRaises(ValueError):
            linear_combination([v1, v2], [1.0, 2.0])

        print(f"\n{Fore.CYAN}Test: Vecteurs de dimensions "
              f"différentes{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} "
              f"linear_combination([v1, v2], [1, 2])")
        print(f"{Fore.RED}⛔ Exception attendue : ValueError{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✅ Test OK ! "
              f"(Exception levée comme prévu){Style.RESET_ALL}")
        print("-" * 50)

    def test_linear_combination_zero_coefs(self):
        """Test avec tous les coefficients à zéro."""
        v1 = Vector([1.0, 2.0, 3.0])
        v2 = Vector([4.0, 5.0, 6.0])

        result = linear_combination([v1, v2], [0.0, 0.0])
        expected = Vector([0.0, 0.0, 0.0])

        self.print_test("Combinaison Linéaire avec coefficients 0",
                        "linear_combination([v1, v2], [0, 0])",
                        expected.values, result.values)
        self.assertEqual(result.values, expected.values)

    def test_linear_combination_single_vector(self):
        """Test avec un seul vecteur et un seul coefficient."""
        v = Vector([3.0, -1.0, 2.5])

        result = linear_combination([v], [2.0])
        expected = Vector([6.0, -2.0, 5.0])

        self.print_test("Combinaison Linéaire avec un seul vecteur",
                        "linear_combination([v], [2])",
                        expected.values, result.values)
        self.assertEqual(result.values, expected.values)

    def test_linear_combination_negative_coefs(self):
        """Test avec des coefficients négatifs."""
        v1 = Vector([2.0, -3.0, 4.0])
        v2 = Vector([1.0, 5.0, -2.0])

        result = linear_combination([v1, v2], [-1.0, -0.5])
        expected = Vector([-2.0 - 0.5, 3.0 - 2.5, -4.0 + 1.0])

        self.print_test("Combinaison Linéaire avec coefficients négatifs",
                        "linear_combination([v1, v2], [-1, -0.5])",
                        expected.values, result.values)
        self.assertEqual(result.values, expected.values)


if __name__ == "__main__":
    unittest.main(verbosity=1)
