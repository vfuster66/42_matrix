# Exercice 13 - Déterminant d'une Matrice

## Introduction
Le **déterminant** d'une matrice carrée est un scalaire qui nous donne des informations essentielles sur la matrice. Il permet notamment de savoir si une matrice est **inversible** ou non. Le déterminant est utilisé dans plusieurs domaines comme l'algèbre linéaire, l'analyse des transformations linéaires et la résolution de systèmes d'équations.

Si le déterminant d'une matrice est **nul**, alors la matrice est **singulière** (elle ne possède pas d'inverse). Sinon, elle est inversible.

## Notions Mathématiques
Le déterminant est noté **det(A)** pour une matrice **A**.

### Déterminant d'une matrice 2x2
Pour une matrice **2x2** :
\[
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
\]
Le déterminant est calculé par la formule :
\[
\det(A) = ad - bc
\]

### Déterminant d'une matrice 3x3
Pour une matrice **3x3** :
\[
A = \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}
\]
Le déterminant se calcule en utilisant l'expansion par les cofacteurs :
\[
\det(A) = a \begin{vmatrix} e & f \\ h & i \end{vmatrix} - b \begin{vmatrix} d & f \\ g & i \end{vmatrix} + c \begin{vmatrix} d & e \\ g & h \end{vmatrix}
\]

### Déterminant pour une matrice NxN
Pour une matrice de taille **n x n**, on utilise la **récurrence** en appliquant la **règle de Laplace** :
\[
\det(A) = \sum (-1)^{i+j} a_{ij} M_{ij}
\]
Où **M_{ij}** est le **mineur** (le déterminant de la sous-matrice obtenue en supprimant la ligne et la colonne de **a_{ij}**).

## Implémentation en Python
Nous allons implémenter le déterminant d'une matrice avec une approche récursive :

```python
def determinant(matrix):
    """
    Calcule le déterminant d'une matrice carrée.
    """
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for col in range(len(matrix)):
        sub_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub_matrix)
    return det
```

Cette fonction :
- Retourne directement l'élément si la matrice est **1x1**.
- Applique la formule du déterminant de **2x2**.
- Utilise la **récursion** et l'expansion par les cofacteurs pour une matrice **NxN**.

## Exemple d'Utilisation
```python
matrix_2x2 = [[3, 8], [4, 6]]
print(determinant(matrix_2x2))  # -14

matrix_3x3 = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
print(determinant(matrix_3x3))  # -306
```

## Applications du Déterminant
- **Vérification de l'inversibilité** d'une matrice.
- **Calcul du volume** dans des espaces multidimensionnels.
- **Systèmes d'équations linéaires** (Règle de Cramer).
- **Transformation géométrique** (rotation, changement d'axes).

## Références
- [Math for Programmers - Amit Patel](https://amitness.com/posts/math-for-programmers)
- [Khan Academy - Déterminant](https://www.khanacademy.org/math/linear-algebra/matrix-transformations/determinant-depth/v/linear-algebra-determinant-intuition)

