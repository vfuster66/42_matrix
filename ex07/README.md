# Exercice 07 - Matrices et Transformations Linéaires

## Introduction
Dans cet exercice, nous allons explorer le concept des **matrices** et leur rôle en tant que transformations linéaires. Une matrice peut être utilisée pour transformer des vecteurs de diverses manières, y compris des rotations, des mises à l'échelle et des translations.

---

## Concepts Mathématiques
### 1. Matrice et transformation linéaire
Une **matrice** est un tableau de nombres organisé en lignes et en colonnes. Elle est souvent utilisée pour décrire des transformations appliquées à des vecteurs.

Une transformation linéaire est une fonction qui préserve **l'addition** et **la multiplication par un scalaire**. Une matrice carrée de dimension (n, n) peut agir sur un vecteur de dimension (n, 1) et renvoyer un vecteur transformé.

**Multiplication d'une matrice par un vecteur :**
\[
 \begin{bmatrix} a & b \\ c & d \end{bmatrix} \times \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} ax + by \\ cx + dy \end{bmatrix}
\]

**Exemple d'une rotation de 90° dans le plan :**
\[
 R = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
\]

Lorsqu'on applique cette matrice à un vecteur \( (x, y) \), on obtient :
\[
 \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \times \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} -y \\ x \end{bmatrix}
\]
Cela signifie que le point a été tourné de 90° dans le sens anti-horaire.

---

## Implémentation en Python
### 1. Représentation d'une matrice
En Python, une matrice est souvent représentée par une **liste de listes** :
```python
A = [[2, 3],
     [4, 5]]
```

### 2. Multiplication d'une matrice par un vecteur
```python
def matrix_vector_mult(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]
```

Exemple d'utilisation :
```python
A = [[0, -1], [1, 0]]  # Matrice de rotation de 90 degrés
v = [3, 4]  # Vecteur initial
result = matrix_vector_mult(A, v)
print(result)  # [-4, 3]
```

---

## Applications
- **Graphismes et animations** : transformations d'objets dans un espace 2D ou 3D.
- **Vision par ordinateur** : correction d'image, reconnaissance de formes.
- **Physique et simulations** : modélisation des mouvements et des forces.
- **Machine Learning** : manipulation des données sous forme de matrices pour l'entraînement des réseaux de neurones.

---

## Résumé
- Une **matrice** peut être utilisée pour appliquer des transformations linéaires sur un vecteur.
- Les transformations linéaires conservent l'addition et la multiplication par un scalaire.
- La multiplication matrice-vecteur s'effectue en combinant lignes et colonnes.
- Ce concept est essentiel dans de nombreux domaines en informatique et en mathématiques.

---

## Pour aller plus loin
- [Math for Programmers - Amit Patel](https://amitness.com/posts/math-for-programmers)
- [3Blue1Brown - Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDOjMrKFR2z6lUO3N58ay1-)
- [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)