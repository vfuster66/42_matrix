# Enter the Matrix

## Introduction
Bienvenue dans **Enter the Matrix**, une série d'exercices sur l'algèbre linéaire en Python. Ce projet vise à comprendre et manipuler les vecteurs, les matrices et d'autres concepts mathématiques essentiels en informatique. Chaque exercice est expliqué de manière détaillée, avec une traduction en programmation.

---

## Utilisation du Makefile
Le projet utilise un **Makefile** pour automatiser certaines commandes Docker. Voici les principales commandes :

- **Compilation de l'image Docker** :
  ```sh
  make build
  ```
  Cela crée une image Docker avec l'environnement nécessaire.

- **Exécuter un test spécifique** :
  ```sh
  make test EX=nom_du_test
  ```
  Remplace `nom_du_test` par le nom du fichier de test.

- **Exécuter tous les tests** :
  ```sh
  make test_all
  ```
  Cette commande lance tous les tests unitaires.

- **Nettoyage des conteneurs inutilisés** :
  ```sh
  make clean
  ```

- **Supprimer l'image Docker** :
  ```sh
  make purge
  ```
  Attention, cela supprimera l'image Docker !

---

## Explications des exercices

### Exercice 00 - Addition, Soustraction et Mise à l’échelle
- Un **vecteur** est une liste ordonnée de nombres.
- Une **matrice** est un tableau bidimensionnel de nombres.
- Addition et soustraction : **opérations élémentaires** entre vecteurs/matrices.
- Mise à l’échelle : **multiplication d’un vecteur ou d’une matrice par un scalaire**.

### Exercice 01 - Combinaison Linéaire
- Une **combinaison linéaire** est une somme pondérée de vecteurs.
- En programmation : **multiplication de chaque vecteur par un coefficient** et somme des résultats.

### Exercice 02 - Interpolation Linéaire (LERP)
- Calcul d’une **valeur intermédiaire** entre deux points.
- Formule informatique :
  ```python
  lerp(a, b, t) = a + (b - a) * t
  ```

### Exercice 03 - Produit Scalaire
- **Produit scalaire** : mesure la projection d’un vecteur sur un autre.
- En programmation : somme des produits élément par élément.

### Exercice 04 - Norme d’un Vecteur
- **Norme** : longueur d’un vecteur.
- Formule :
  ```python
  norm = sqrt(x1**2 + x2**2 + ... + xn**2)
  ```

### Exercice 05 - Cosinus de l’Angle entre deux Vecteurs
- Formule :
  ```python
  cos_theta = dot_product(v1, v2) / (norm(v1) * norm(v2))
  ```
- Permet de mesurer **l’alignement entre deux vecteurs**.

### Exercice 06 - Produit Vectoriel
- Produit donnant un vecteur **perpendiculaire** aux deux autres en 3D.
- Formule informatique :
  ```python
  cross_product = [y1*z2 - y2*z1, z1*x2 - z2*x1, x1*y2 - x2*y1]
  ```

### Exercice 07 - Matrices et Transformations Linéaires
- Une **matrice** représente une **transformation linéaire**.
- En programmation : appliquer une **matrice à un vecteur** par multiplication.

### Exercice 08 - Multiplication Matrice-Matrice
- Le produit matriciel est défini par :
  ```math
  C_{ij} = \sum_{k} A_{ik} B_{kj}
  ```
- Cela permet de composer plusieurs transformations linéaires.

### Exercice 09 - Matrices Carrées et Identité
- Une **matrice carrée** a un même nombre de lignes et colonnes.
- Une **matrice identité** a des `1` sur la diagonale et `0` ailleurs.
- Multiplication avec l’identité : **ne change pas la matrice**.

### Exercice 10 - Trace d’une Matrice
- La **trace** est la **somme des éléments de la diagonale principale**.
- Utilisée en algèbre linéaire et en optimisation.

### Exercice 11 - Matrice Transposée
- La **transposée** d’une matrice échange ses lignes et ses colonnes.
- Code Python :
  ```python
  transpose = list(zip(*matrix))
  ```

### Exercice 12 - Matrice Échelonnée
- Réduction par **opérations élémentaires sur les lignes**.
- Utilisée pour **résoudre des systèmes linéaires** efficacement.

### Exercice 13 - Déterminant d’une Matrice
- Le **déterminant** est un **scalaire** indiquant si une matrice est inversible.
- Déterminant nul = **matrice non inversible**.
- Calculé récursivement par **développement par les mineurs**.

### Exercice 14 - Matrice de Projection (Bonus)
- Application aux **transformations 3D**.
- **Utilisation du software** :
  - Générer un fichier `.proj` :
    ```sh
    python3 -m ex14.generate_proj
    ```
  - Afficher le projet :
    ```sh
    ./display
    ```
  - Un README spécifique dans le dossier **explique le fonctionnement du software**.

### Exercice 15 - Espaces Vectoriels Complexes (Bonus)
- Introduction aux **nombres complexes en algèbre linéaire**.
- Un **nombre complexe** est de la forme `a + bi`.
- Exemple en Python :
  ```python
  complex_matrix = [[complex(1, 2), complex(3, -1)], [complex(-2, 4), complex(0, 3)]]
  ```
- Utile pour la **physique quantique et l’analyse des signaux**.

---

## Sources et références
- [Math for Programmers - Amit Patel](https://amitness.com/posts/math-for-programmers)
- [3Blue1Brown - Linear Algebra Playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDOjMrKFR2z6lUO3N58ay1-)
- [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)

---

## Conclusion
Ce projet permet de **comprendre l'algèbre linéaire par la pratique** en Python. Chaque exercice introduit une nouvelle notion avec des **applications concrètes**. 🚀

