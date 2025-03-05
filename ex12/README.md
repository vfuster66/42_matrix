# Exercice 12 - Matrice Échelonnée

## Introduction

Dans cet exercice, nous allons explorer la **mise sous forme échelonnée** d'une matrice, un processus fondamental en algèbre linéaire. Cette transformation permet de simplifier la résolution des systèmes d'équations linéaires, de calculer le rang d'une matrice et de déterminer si elle est inversible.

---

## Concepts Mathématiques

### 1. Définition
Une matrice est dite **échelonnée par lignes** lorsque :
- Tous les éléments non nuls d'une ligne sont situés à droite de ceux de la ligne précédente.
- Toute ligne composée uniquement de zéros est placée en bas de la matrice.

Une matrice est en **forme échelonnée réduite** (Row Echelon Form - REF) si, en plus des conditions précédentes :
- Le premier élément non nul de chaque ligne est égal à 1 (appelé **pivot**).
- Tous les pivots sont les seuls nombres non nuls de leur colonne.

### 2. Opérations élémentaires
Pour mettre une matrice sous forme échelonnée, on peut utiliser les **opérations élémentaires** suivantes :
- **Interchanger deux lignes**
- **Multiplier une ligne par un scalaire non nul**
- **Ajouter ou soustraire un multiple d'une ligne à une autre ligne**

### 3. Exemple de réduction 
Prenons la matrice suivante :

\[ \begin{bmatrix} 2 & 4 & -2 \\ -4 & -6 & 10 \\ 6 & 8 & 0 \end{bmatrix} \]

1. Diviser la première ligne par 2 :
   \[ \begin{bmatrix} 1 & 2 & -1 \\ -4 & -6 & 10 \\ 6 & 8 & 0 \end{bmatrix} \]
2. Ajouter 4 fois la première ligne à la deuxième :
   \[ \begin{bmatrix} 1 & 2 & -1 \\ 0 & 2 & 6 \\ 6 & 8 & 0 \end{bmatrix} \]
3. Soustraire 6 fois la première ligne à la troisième :
   \[ \begin{bmatrix} 1 & 2 & -1 \\ 0 & 2 & 6 \\ 0 & -4 & 6 \end{bmatrix} \]
4. Diviser la deuxième ligne par 2 :
   \[ \begin{bmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \\ 0 & -4 & 6 \end{bmatrix} \]
5. Ajouter 4 fois la deuxième ligne à la troisième :
   \[ \begin{bmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \\ 0 & 0 & 18 \end{bmatrix} \]

La matrice est maintenant sous **forme échelonnée**.

---

## Implémentation en Python
Nous allons créer une fonction `row_echelon(matrix)` pour transformer une matrice en forme échelonnée :

```python
import numpy as np

def row_echelon(matrix):
    mat = np.array(matrix, dtype=float)
    rows, cols = mat.shape
    lead = 0
    
    for r in range(rows):
        if lead >= cols:
            return mat
        i = r
        while mat[i, lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if cols == lead:
                    return mat
        mat[[i, r]] = mat[[r, i]]
        mat[r] = mat[r] / mat[r, lead]
        for i in range(rows):
            if i != r:
                mat[i] -= mat[i, lead] * mat[r]
        lead += 1
    
    return mat
```

### Exemple d'utilisation
```python
matrix = [[2, 4, -2], [-4, -6, 10], [6, 8, 0]]
print(row_echelon(matrix))
```

---

## Applications Pratiques
- **Résolution de systèmes linéaires** : La forme échelonnée permet d'extraire les solutions plus facilement.
- **Calcul du rang d'une matrice** : Le nombre de lignes non nulles dans la matrice échelonnée donne le rang.
- **Détection de matrices singulières** : Une matrice échelonnée ayant une ligne de zéros signifie que le système a des solutions infinies ou aucune solution.

---

## Sources et Références
- [Math for Programmers - Amit Patel](https://amitness.com/posts/math-for-programmers)
- [Khan Academy - Gaussian Elimination](https://www.khanacademy.org/math/linear-algebra/matrix-transformations/row-echelon-form/v/reduced-row-echelon-form)
- [3Blue1Brown - Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDOjMrKFR2z6lUO3N58ay1-)

---

## Conclusion
Cet exercice permet de comprendre la réduction des matrices en forme échelonnée, une opération fondamentale en algèbre linéaire. En programmant cette transformation en Python, nous faisons le lien entre **mathématiques abstraites et applications concrètes**. 🚀