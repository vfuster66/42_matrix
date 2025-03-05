# Exercice 10 - Trace d'une Matrice

## Introduction
La **trace d'une matrice** est une notion fondamentale en algèbre linéaire. Elle correspond à la somme des éléments situés sur la diagonale principale d'une matrice carrée. Cette opération est utile dans plusieurs domaines, comme l'optimisation, les transformations linéaires et la physique quantique.

## Définition Mathématique
Soit \( A \) une matrice carrée \( n \times n \), la trace de \( A \), notée \( \text{Tr}(A) \), est définie comme :
\[
\text{Tr}(A) = \sum_{i=1}^{n} A_{ii}
\]

Autrement dit, on additionne tous les éléments \( A_{ii} \) où \( i \) correspond à l'indice de ligne et de colonne.

### Exemple Mathématique
Si nous avons la matrice suivante :
\[
A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}
\]

Alors, la trace est :
\[
\text{Tr}(A) = 1 + 5 + 9 = 15
\]

## Implémentation en Python
L'implémentation en Python de la trace d'une matrice est simple. Il suffit de parcourir la diagonale principale et d'additionner ses éléments.

### Exemple de Code
```python
class Matrix:
    def __init__(self, values):
        self.values = values
        self.n = len(values)  # Nombre de lignes

    def trace(self):
        return sum(self.values[i][i] for i in range(self.n))

# Exemple d'utilisation
matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Trace de la matrice :", matrix.trace())  # Affiche 15
```

## Applications
La trace d'une matrice est utilisée dans plusieurs domaines :
- **Optimisation et algorithmes de Machine Learning** : la trace apparaît dans certaines fonctions de coût.
- **Calcul des invariants** : en physique et en mathématiques, la trace est utilisée pour caractériser des transformations linéaires.
- **Probabilités et statistiques** : la trace joue un rôle dans la représentation des matrices de covariance.
- **Graphes et réseaux** : en théorie des graphes, la trace est utilisée pour calculer certaines propriétés des matrices d'adjacence.

## Conclusion
L'opération de trace est une manière simple mais puissante d'extraire une information clé d'une matrice carrée. Elle permet notamment d'évaluer certaines transformations linéaires et intervient dans de nombreux domaines scientifiques et techniques.

---

### Références
- [Math for Programmers - Amit Patel](https://amitness.com/posts/math-for-programmers)
- [Khan Academy - Matrices et Transformations](https://www.khanacademy.org/math/linear-algebra)

