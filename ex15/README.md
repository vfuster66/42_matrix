# Exercice 15 - Espaces Vectoriels Complexes

## Introduction

Cet exercice explore l'algèbre linéaire dans le domaine des **nombres complexes**. Contrairement aux nombres réels, les nombres complexes incluent une partie imaginaire et sont essentiels dans plusieurs domaines comme la **physique quantique**, le **traitement du signal** et l'**électromagnétisme**.

---

## Notions Mathématiques

### 1. Nombres Complexes
Un nombre complexe est défini comme :
\[ z = a + bi \]
- **a** : partie réelle
- **b** : partie imaginaire
- **i** : unité imaginaire avec \( i^2 = -1 \)

En Python, on utilise le type `complex` :
```python
z1 = complex(3, 4)  # 3 + 4i
z2 = complex(1, -2) # 1 - 2i
```

### 2. Addition et Multiplication Complexes
- **Addition** : \( (a + bi) + (c + di) = (a+c) + (b+d)i \)
- **Multiplication** : \( (a + bi) \times (c + di) = (ac - bd) + (ad + bc)i \)

En Python :
```python
z3 = z1 + z2
z4 = z1 * z2
```

### 3. Matrices Complexes
Une matrice complexe est une matrice dont les éléments sont des nombres complexes.
Exemple :
\[
\begin{bmatrix}
1 + 2i & 3 - i \\
-2 + 4i & 0 + 3i
\end{bmatrix}
\]

### 4. Conjugué et Module
- **Conjugué** : \( \overline{z} = a - bi \)
- **Module** : \( |z| = \sqrt{a^2 + b^2} \)

En Python :
```python
conj_z1 = z1.conjugate()
mod_z1 = abs(z1)
```

---

## Implémentation en Python

### 1. Création d'une Matrice Complexe
```python
matrix = [[complex(1, 2), complex(3, -1)], [complex(-2, 4), complex(0, 3)]]
```

### 2. Produit Matrice-Vecteur
Pour multiplier une matrice complexe par un vecteur complexe :
```python
def mul_matrix_vector(matrix, vector):
    return [sum(m * v for m, v in zip(row, vector)) for row in matrix]
```

### 3. Produit Matrice-Matrice
```python
def mul_matrix_matrix(A, B):
    size = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(size)) for j in range(size)] for i in range(size)]
```

---

## Objectifs de l'Exercice
1. **Manipuler les nombres complexes** en Python.
2. **Réaliser des opérations matricielles complexes** :
   - Somme et produit de matrices
   - Produit matrice-vecteur
   - Calcul du déterminant et de l'inverse
3. **Appliquer ces concepts à des problèmes pratiques** en physique et ingénierie.

---

## Tests et Vérifications
Pour exécuter les tests :
```sh
make test EX=15
```

Pour tester manuellement en Python :
```python
from ex15.complex_matrix import mul_matrix_matrix
A = [[complex(1, 2), complex(3, -1)], [complex(-2, 4), complex(0, 3)]]
B = [[complex(0, 1), complex(2, -2)], [complex(1, 3), complex(-1, 0)]]
print(mul_matrix_matrix(A, B))
```

---

## Sources et Références
- [Math for Programmers - Amit Patel](https://amitness.com/posts/math-for-programmers)
- [3Blue1Brown - Introduction aux Nombres Complexes](https://www.youtube.com/watch?v=T647CGsuOVU)
- [Khan Academy - Complex Numbers](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:complex/x2f8bb11595b61c86:complex-intro/v/complex-numbers-introduction)

---

## Conclusion
Cet exercice introduit les **espaces vectoriels complexes**, une extension puissante des concepts d’algèbre linéaire. Il fournit les bases pour des applications avancées en physique et en mathématiques appliquées. 🚀