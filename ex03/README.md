# Exercice 03 - Produit Scalaire

## Introduction

Le **produit scalaire** est une opération fondamentale en algèbre linéaire qui mesure l'alignement de deux vecteurs. En programmation, il est souvent utilisé pour le calcul d’angles, les projections et l'optimisation en apprentissage automatique.

---

## Explication Mathématique

Le produit scalaire de deux vecteurs \( v_1 \) et \( v_2 \) est défini comme :

\[
v_1 \cdot v_2 = \sum_{i=1}^{n} v_{1i} \times v_{2i}
\]

Où :
- \( v_1 = [x_1, x_2, ..., x_n] \) et \( v_2 = [y_1, y_2, ..., y_n] \) sont des vecteurs de même dimension.
- Le produit scalaire est la somme des produits des composantes correspondantes des vecteurs.

### Exemple
Si nous avons deux vecteurs en 3D :
\[
v_1 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \quad v_2 = \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}
\]
Le produit scalaire est :
\[
1 \times 4 + 2 \times 5 + 3 \times 6 = 4 + 10 + 18 = 32
\]

Le produit scalaire donne un **nombre réel** et non un vecteur.

---

## Implémentation en Python

Nous pouvons implémenter le produit scalaire de plusieurs manières :

### Avec des listes Python
```python
from typing import List

def dot_product(v1: List[float], v2: List[float]) -> float:
    """Calcule le produit scalaire de deux vecteurs."""
    return sum(x * y for x, y in zip(v1, v2))

# Exemple d'utilisation
v1 = [1, 2, 3]
v2 = [4, 5, 6]
print(dot_product(v1, v2))  # Output: 32
```

### Avec NumPy (plus performant pour des vecteurs de grande taille)
```python
import numpy as np

def dot_product_numpy(v1: np.ndarray, v2: np.ndarray) -> float:
    """Produit scalaire avec NumPy."""
    return np.dot(v1, v2)

# Exemple d'utilisation
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(dot_product_numpy(v1, v2))  # Output: 32
```

NumPy est recommandé pour **traiter des données volumineuses plus rapidement**.

---

## Applications en Informatique

- **Calcul de l’angle entre deux vecteurs** :
  \[
  \cos(\theta) = \frac{v_1 \cdot v_2}{||v_1|| \times ||v_2||}
  \]
  Cela permet de mesurer la similarité entre deux vecteurs.

- **Vision par ordinateur** : Utilisé pour détecter les contours et la direction des objets.
- **Réseaux de neurones** : Permet d’évaluer la similarité entre des données.
- **Mécanique et physique** : Détermine si une force agit dans la direction d’un objet.
- **Recommandation de contenu** : Mesure la proximité entre des profils utilisateurs et des éléments recommandés.

---

## Conclusion

Le produit scalaire est un concept clé en algèbre linéaire et en informatique. Il permet de **calculer des projections, mesurer des similarités et résoudre des problèmes d'optimisation**. Une bonne compréhension de cette opération est essentielle pour progresser en machine learning, en graphisme et en physique.

---

## Sources et Références
- [Math for Programmers - Amit Patel](https://amitness.com/posts/math-for-programmers)
- [3Blue1Brown - Dot Product Visualization](https://www.youtube.com/watch?v=LyGKycYT2v0)
- [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)