# Exercice 01 - Combinaison Linéaire

## Introduction
Dans cet exercice, nous allons explorer le concept de **combinaison linéaire**, un des fondements de l'algèbre linéaire. Il s'agit d'une opération qui consiste à additionner plusieurs vecteurs après les avoir multipliés par des coefficients (scalaires). Cette opération est très utile en informatique, notamment en **intelligence artificielle**, en **graphisme 3D** et en **analyse de données**.

---

## Explication Mathématique

Une **combinaison linéaire** de vecteurs est définie comme suit :

\[ V = a_1 \times v_1 + a_2 \times v_2 + \dots + a_n \times v_n \]

Où :
- \( v_1, v_2, \dots, v_n \) sont des vecteurs,
- \( a_1, a_2, \dots, a_n \) sont des scalaires (nombres réels ou complexes),
- \( V \) est le résultat de la combinaison linéaire.

Par exemple, si nous avons deux vecteurs en 2D :
\[
v_1 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}, \quad v_2 = \begin{bmatrix} 3 \\ 4 \end{bmatrix}
\]
Et que nous les combinons avec les scalaires \( 2 \) et \( -1 \) :
\[
V = 2 \times \begin{bmatrix} 1 \\ 2 \end{bmatrix} + (-1) \times \begin{bmatrix} 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 2 \\ 4 \end{bmatrix} + \begin{bmatrix} -3 \\ -4 \end{bmatrix} = \begin{bmatrix} -1 \\ 0 \end{bmatrix}
\]

Cette opération permet de **créer de nouveaux vecteurs à partir de vecteurs existants**, ce qui est utile pour représenter des transformations et des relations linéaires entre données.

---

## Implémentation en Python

En Python, nous pouvons utiliser des **listes** ou des **NumPy arrays** pour représenter les vecteurs et effectuer les opérations de combinaison linéaire.

### Avec des listes Python :
```python
from typing import List

def linear_combination(vectors: List[List[float]], scalars: List[float]) -> List[float]:
    """
    Calcule une combinaison linéaire de vecteurs.
    """
    result = [0] * len(vectors[0])
    for scalar, vector in zip(scalars, vectors):
        result = [res + scalar * val for res, val in zip(result, vector)]
    return result

# Exemple d'utilisation
vectors = [[1, 2], [3, 4]]
scalars = [2, -1]
print(linear_combination(vectors, scalars))  # Output: [-1, 0]
```

### Avec NumPy :
```python
import numpy as np

def linear_combination_numpy(vectors: np.ndarray, scalars: np.ndarray) -> np.ndarray:
    """
    Calcule une combinaison linéaire de vecteurs avec NumPy.
    """
    return np.sum(scalars[:, np.newaxis] * vectors, axis=0)

# Exemple d'utilisation
vectors = np.array([[1, 2], [3, 4]])
scalars = np.array([2, -1])
print(linear_combination_numpy(vectors, scalars))  # Output: [-1  0]
```

L'avantage d'utiliser **NumPy** est que les calculs sont optimisés et plus rapides pour de grandes quantités de données.

---

## Applications en Informatique

- **Intelligence Artificielle** : Les combinaisons linéaires sont au cœur des **réseaux de neurones** (produit pondéré des entrées d'un neurone).
- **Graphisme 3D** : Utilisé pour le **morphing**, la déformation d'objets et la transformation de modèles.
- **Compression de Données** : Techniques comme l'**Analyse en Composantes Principales (PCA)** se basent sur des combinaisons linéaires de données pour réduire la dimensionnalité.

---

## Conclusion
La combinaison linéaire est une notion fondamentale en **algèbre linéaire** et en informatique. Elle permet de **manipuler des vecteurs et d'effectuer des transformations utiles** dans plusieurs domaines. Cet exercice nous apprend à comprendre comment les scalaires influencent les vecteurs et comment les combiner efficacement en programmation.

---

## Sources et Références
- [Math for Programmers - Amit Patel](https://amitness.com/posts/math-for-programmers)
- [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [3Blue1Brown - Linear Algebra Playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDOjMrKFR2z6lUO3N58ay1-)