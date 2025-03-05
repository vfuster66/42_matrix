# Exercice 00 - Addition, Soustraction et Mise à l’échelle des Vecteurs et Matrices

## Introduction
Dans cet exercice, nous allons nous familiariser avec les opérations de base sur les vecteurs et les matrices en algèbre linéaire. Ces opérations sont essentielles pour la programmation scientifique, la 3D, et l'intelligence artificielle.

Nous aborderons trois opérations fondamentales :
- **L'addition** de vecteurs et de matrices
- **La soustraction** de vecteurs et de matrices
- **La mise à l’échelle** (multiplication par un scalaire)

## Notions Mathématiques

### 1. Qu'est-ce qu'un vecteur ?
Un vecteur est une liste ordonnée de nombres réels (ou complexes) qui représente une grandeur ayant une **direction** et une **norme**.
Exemple d'un vecteur en dimension 3 :
\[ \mathbf{v} = \begin{bmatrix} 2 \\ -1 \\ 3 \end{bmatrix} \]

### 2. Qu'est-ce qu'une matrice ?
Une matrice est un tableau rectangulaire de nombres organisés en **lignes** et **colonnes**.
Exemple de matrice 2x2 :
\[ A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \]

### 3. Addition et soustraction
L'addition et la soustraction de vecteurs et de matrices se font **composant par composant**. 

#### Pour les vecteurs :
\[ \mathbf{a} + \mathbf{b} = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} + \begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} a_1 + b_1 \\ a_2 + b_2 \end{bmatrix} \]

#### Pour les matrices :
\[ A + B = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} + \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix} = \begin{bmatrix} a_{11} + b_{11} & a_{12} + b_{12} \\ a_{21} + b_{21} & a_{22} + b_{22} \end{bmatrix} \]

### 4. Mise à l'échelle (multiplication par un scalaire)
Multiplier un vecteur ou une matrice par un **scalaire** (nombre) revient à multiplier chaque composant :

#### Pour un vecteur :
\[ \lambda \mathbf{v} = \lambda \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} = \begin{bmatrix} \lambda v_1 \\ \lambda v_2 \\ \lambda v_3 \end{bmatrix} \]

#### Pour une matrice :
\[ \lambda A = \lambda \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} = \begin{bmatrix} \lambda a_{11} & \lambda a_{12} \\ \lambda a_{21} & \lambda a_{22} \end{bmatrix} \]

---

## Implémentation en Python

### Addition et soustraction de vecteurs
```python
class Vector:
    def __init__(self, values):
        self.values = values
    
    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.values, other.values)])
    
    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.values, other.values)])
    
    def __mul__(self, scalar):
        return Vector([scalar * a for a in self.values])
    
    def __repr__(self):
        return f"Vector({self.values})"

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1 + v2)  # Vector([5, 7, 9])
print(v1 - v2)  # Vector([-3, -3, -3])
print(v1 * 2)   # Vector([2, 4, 6])
```

### Addition et soustraction de matrices
```python
class Matrix:
    def __init__(self, values):
        self.values = values
    
    def __add__(self, other):
        return Matrix([[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.values, other.values)])
    
    def __sub__(self, other):
        return Matrix([[a - b for a, b in zip(row1, row2)] for row1, row2 in zip(self.values, other.values)])
    
    def __mul__(self, scalar):
        return Matrix([[scalar * a for a in row] for row in self.values])
    
    def __repr__(self):
        return f"Matrix({self.values})"

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])
print(A + B)  # Matrix([[6, 8], [10, 12]])
print(A - B)  # Matrix([[-4, -4], [-4, -4]])
print(A * 2)  # Matrix([[2, 4], [6, 8]])
```

---

## Applications en Informatique
- **Graphismes 3D** : manipulation de vecteurs pour les transformations graphiques.
- **Calcul scientifique** : résolution de problèmes physiques et ingénierie.
- **Intelligence artificielle** : manipulation des poids et matrices dans les réseaux de neurones.

---

## Récapitulatif
- Addition et soustraction : composant par composant.
- Multiplication par un scalaire : chaque composant multiplié par le scalaire.
- Utilisation en **3D, IA et modélisation mathématique**.

Sources et lectures recommandées :
- [Math for Programmers - Amit Patel](https://amitness.com/posts/math-for-programmers)
- [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [3Blue1Brown - Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDOjMrKFR2z6lUO3N58ay1-)

---

## Conclusion
Cet exercice permet de comprendre les opérations fondamentales en algèbre linéaire et leur application en programmation.