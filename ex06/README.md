# Exercice 06 - Produit Vectoriel

## Introduction
Le **produit vectoriel** est une opération définie pour les vecteurs en trois dimensions. Il permet d'obtenir un vecteur **perpendiculaire** aux deux vecteurs d'origine, ce qui est largement utilisé en physique, en graphisme 3D et en mécanique.

---

## 1. Notion Mathématique
Le produit vectoriel de deux vecteurs \( \mathbf{v_1} \) et \( \mathbf{v_2} \) dans \( \mathbb{R}^3 \) est défini par :

\[
\mathbf{v_1} \times \mathbf{v_2} =
\begin{bmatrix}
  y_1 z_2 - y_2 z_1 \\
  z_1 x_2 - z_2 x_1 \\
  x_1 y_2 - x_2 y_1
\end{bmatrix}
\]

Où :
- \( (x_1, y_1, z_1) \) et \( (x_2, y_2, z_2) \) sont les coordonnées des vecteurs \( \mathbf{v_1} \) et \( \mathbf{v_2} \).
- Le **résultat est un vecteur orthogonal** aux deux vecteurs d’origine.

Le produit vectoriel est utile pour :
- Trouver un vecteur normal à un plan.
- Calculer des moments et des forces en physique.
- Déterminer la direction de la rotation d’un objet.

---

## 2. Traduction en Programmation
En informatique, nous pouvons coder le produit vectoriel en Python de la manière suivante :

```python
def cross_product(v1, v2):
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

# Exemple d'utilisation
v1 = [1, 2, 3]
v2 = [4, 5, 6]

print(cross_product(v1, v2))  # [-3, 6, -3]
```

Python offre aussi une méthode native via `numpy` :

```python
import numpy as np
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(np.cross(v1, v2))  # [-3, 6, -3]
```

---

## 3. Applications en Informatique
Le produit vectoriel est largement utilisé dans plusieurs domaines :
- **Graphisme 3D** : Calcul des normales des surfaces pour l’éclairage.
- **Physique et mécanique** : Calcul des forces et des rotations.
- **Navigation et robotique** : Détermination des axes de rotation.

---

## 4. Résumé
- Le produit vectoriel retourne un vecteur **perpendiculaire** aux deux vecteurs donnés.
- Il est calculé grâce à une matrice déterminant.
- Il est utilisé en **3D, mécanique, physique et graphisme**.
- Python permet de l’implémenter avec `numpy` pour simplifier les calculs.

---

## Sources et Références
- [Math for Programmers - Amit Patel](https://amitness.com/posts/math-for-programmers)
- [Khan Academy - Produit Vectoriel](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/dot-cross-products/v/defining-the-cross-product)
- [Wikipedia - Produit Vectoriel](https://fr.wikipedia.org/wiki/Produit_vectoriel)

---
