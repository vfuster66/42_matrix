# Exercice 09 - Matrices Carrées et Identité

## Introduction
Dans cet exercice, nous allons explorer les **matrices carrées** et la **matrice identité**. Ces concepts sont fondamentaux en algèbre linéaire et ont de nombreuses applications en informatique, notamment dans les transformations linéaires et les systèmes d'équations.

---

## Notions Mathématiques

### 1. Matrice Carrée
Une **matrice carrée** est une matrice qui a le même nombre de lignes et de colonnes. Elle est notée :

\[
A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix}
\]

Si une matrice est carrée, elle possède une diagonale principale, c'est-à-dire les éléments \(a_{ii}\) situés de haut en bas.

### 2. Matrice Identité
Une **matrice identité** est une matrice carrée particulière qui a des `1` sur sa diagonale principale et des `0` ailleurs :

\[
I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\]

Cette matrice est **l'élément neutre** de la multiplication matricielle, ce qui signifie que pour toute matrice carrée \(A\) :

\[
A \times I = I \times A = A
\]

Cela fonctionne comme le chiffre `1` pour la multiplication classique.

---

## Implémentation en Python
Nous allons maintenant traduire ces notions en code Python.

### 1. Créer une Matrice Identité
En Python, on peut générer une matrice identité avec `numpy` :

```python
import numpy as np

# Créer une matrice identité de taille 3x3
I = np.eye(3)
print(I)
```

Sortie :
```
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

### 2. Vérifier la Propriété de l'Identité
On peut tester que la multiplication par la matrice identité ne change pas la matrice :

```python
A = np.array([[3, 2, 1], [4, 5, 6], [7, 8, 9]])
result = np.dot(A, I)  # Multiplication matricielle
print(result)
```

Sortie :
```
[[3. 2. 1.]
 [4. 5. 6.]
 [7. 8. 9.]]
```
Comme attendu, la matrice reste inchangée.

---

## Applications en Informatique
Les matrices carrées et la matrice identité ont plusieurs applications importantes :

- **Transformations linéaires** : Utilisées en graphique 3D pour appliquer des rotations et des changements d'échelle.
- **Résolution de systèmes d'équations linéaires** : La matrice identité est utilisée dans les méthodes de réduction pour trouver des solutions.
- **Apprentissage automatique** : Les matrices identités sont souvent impliquées dans l'initialisation des poids dans les réseaux neuronaux.

---

## Conclusion
Dans cet exercice, nous avons appris ce qu'est une matrice carrée et à quoi sert la matrice identité. Nous avons vu que cette dernière joue un rôle essentiel dans les opérations matricielles et nous avons illustré son utilisation en Python.
