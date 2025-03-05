import unittest
from ex04.vector import Vector
from colorama import Fore, Style


class TestVectorNorms(unittest.TestCase):

    def print_test(self, test_name, operation, expected, obtained):
        """Affichage amélioré du test."""
        print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Opération :{Style.RESET_ALL} {operation}")
        print(f"{Fore.GREEN}Résultat attendu :{Style.RESET_ALL} {expected}")
        print(f"{Fore.BLUE}Résultat obtenu  :{Style.RESET_ALL} {obtained}")

        if round(expected, 6) == round(obtained, 6):
            print(f"{Fore.GREEN}✅ Test OK !{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Test ÉCHOUÉ !{Style.RESET_ALL}")
        print("-" * 50)

    def test_norms(self):
        """Test des différentes normes avec plusieurs vecteurs."""
        cases = [
            (Vector([0.0, 0.0, 0.0]), (0.0, 0.0, 0.0)),
            (Vector([1.0, 2.0, 3.0]), (6.0, 3.741657, 3.0)),
            (Vector([-1.0, -2.0]), (3.0, 2.236068, 2.0)),
            (Vector([5.0, -4.0, 3.0]), (12.0, 7.071068, 5.0)),
            (Vector([-10.0, 20.0, -30.0]), (60.0, 37.416574, 30.0)),
            (Vector([1e-10, -1e-10, 2e-10]), (4e-10, (6e-20) ** 0.5, 2e-10)),
            # ✅ Nouveaux tests ajoutés
            (Vector([1e100, -1e100, 2e100]), (4e100, (6e200) ** 0.5, 2e100)),
            (Vector([1.0 / (2 ** 0.5), 1.0 / (2 ** 0.5)]),
             (1.414214, 1.0, 0.707107)),
            (Vector([5.0, 5.0, 5.0]), (15.0, 8.660254, 5.0)),
            (Vector([42.0]), (42.0, 42.0, 42.0)),
            (Vector([-7.0, 3.0, -9.0]), (19.0, (49 + 9 + 81) ** 0.5, 9.0))
        ]

        for vector, (expected_norm1, expected_norm2,
                     expected_norm_inf) in cases:
            self.print_test(
                "Norme 1",
                f"{vector}.norm_1()",
                expected_norm1,
                vector.norm_1()
            )
            self.assertAlmostEqual(vector.norm_1(), expected_norm1, places=6)

            self.print_test(
                "Norme 2", f"{vector}.norm()", expected_norm2, vector.norm()
            )

            if expected_norm2 == 0.0:
                self.assertEqual(vector.norm(), expected_norm2)
            else:
                erreur_relative = abs(vector.norm() - expected_norm2) \
                    / abs(expected_norm2)

                self.assertTrue(
                    erreur_relative < 1e-6,
                    f"Erreur relative trop grande: {erreur_relative}\n"
                    f"Valeur obtenue : {vector.norm()}\n"
                    f"Valeur attendue : {expected_norm2}"
                )

            self.print_test(
                "Norme ∞", f"{vector}.norm_inf()",
                expected_norm_inf, vector.norm_inf()
                )
            self.assertAlmostEqual(vector.norm_inf(),
                                   expected_norm_inf, places=6)

    def test_empty_vector(self):
        """Test sur un vecteur vide."""
        v = Vector([])
        self.assertEqual(v.norm_1(), 0.0)
        self.assertEqual(v.norm(), 0.0)
        self.assertEqual(v.norm_inf(), 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=1)
