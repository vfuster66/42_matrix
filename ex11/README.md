# Exercice 11 - Matrice Transposée

## Introduction
Dans cet exercice, nous allons explorer la notion de **matrice transposée** en algèbre linéaire. La transposition est une opération simple mais très utile, notamment dans les domaines du traitement du signal, de l'apprentissage automatique et des transformations matricielles en géométrie.

---

## Définition Mathématique
La **transposée** d'une matrice \( A \), notée \( A^T \), est obtenue en échangeant ses lignes et ses colonnes.

Si \( A \) est une matrice de taille \( m \times n \), alors \( A^T \) sera une matrice de taille \( n \times m \).

**Exemple :**
\[
A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}
\]

Sa transposée est :
\[
A^T = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}
\]

---

## Implémentation en Python
La transposition d'une matrice en Python peut se faire de plusieurs manières. Voici une implémentation basique :

```python
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def transpose(self):
        return [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]

# Exemple d'utilisation
A = Matrix([[1, 2, 3], [4, 5, 6]])
A_T = A.transpose()
print(A_T)  # [[1, 4], [2, 5], [3, 6]]
```

On peut aussi utiliser **NumPy**, qui propose une méthode optimisée :

```python
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
A_T = A.T
print(A_T)  # [[1 4] [2 5] [3 6]]
```

---

## Applications
- **Traitement d'images** : la transposition peut être utilisée pour faire pivoter des images ou changer l'orientation des pixels.
- **Apprentissage automatique** : dans le calcul des **covariances** et des transformations de données.
- **Systèmes d'équations linéaires** : dans le calcul des solutions en utilisant la décomposition matricielle.
- **Calcul de produits scalaires et produits matriciels** : la transposition joue un rôle essentiel dans les transformations de matrices.

---

## Conclusion
La transposée d'une matrice est une opération simple mais fondamentale en algèbre linéaire et en programmation. Elle est utilisée dans de nombreux domaines scientifiques et techniques. Cet exercice permet de mieux comprendre cette transformation et de l'implémenter efficacement en Python.

---

## Références
- [Math for Programmers - Amit Patel](https://amitness.com/posts/math-for-programmers)
- [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)