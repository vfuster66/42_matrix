# Exercice 08 - Multiplication Matrice-Matrice

## Introduction
La multiplication matricielle est une opération fondamentale en algèbre linéaire et en informatique. Elle est utilisée dans divers domaines tels que la 3D, l'optimisation, et les réseaux neuronaux. Cet exercice consiste à implémenter l'opération de multiplication entre deux matrices.

---

## Notions Mathématiques

### Multiplication de Matrices
La multiplication de matrices est définie comme suit :

Si \( A \) est une matrice de taille \( m \times n \) et \( B \) une matrice de taille \( n \times p \), alors le produit \( C = A \times B \) est une matrice de taille \( m \times p \) définie par :

\[
C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}
\]

Autrement dit, l'entrée \( C_{ij} \) de la matrice résultante est obtenue en faisant le produit scalaire entre la \( i \)-ème ligne de \( A \) et la \( j \)-ème colonne de \( B \).

### Propriétés Importantes
- **Non-commutativité** : En général, \( A \times B \neq B \times A \).
- **Associativité** : \( (A \times B) \times C = A \times (B \times C) \).
- **Distributivité** : \( A \times (B + C) = A \times B + A \times C \).
- **Produit avec la matrice identité** : \( A \times I = A \).

---

## Implémentation en Python
Voici comment traduire la multiplication matricielle en Python :

```python
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Multiplication impossible : dimensions incompatibles")
        
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                   for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)

# Exemple d'utilisation
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[2, 0], [1, 2]])
C = A.multiply(B)
print(C.data)  # [[4, 4], [10, 8]]
```

---

## Applications en Informatique
1. **Graphismes et transformations 3D** : La multiplication de matrices est utilisée pour transformer des objets dans un espace tridimensionnel (rotation, translation, mise à l'échelle).
2. **Réseaux neuronaux** : Les poids d'un réseau de neurones sont souvent représentés par des matrices multipliées par des vecteurs d'entrées.
3. **Systèmes d'équations linéaires** : La multiplication de matrices permet de modéliser et de résoudre des systèmes d'équations linéaires de manière efficace.

---

## Conclusion
Cet exercice permet de comprendre et d'implémenter un concept central de l'algèbre linéaire, utile dans de nombreuses applications informatiques. Il est crucial de bien saisir les règles de multiplication des matrices et leurs propriétés pour les exploiter pleinement dans vos projets.