# Enter the Matrix

## Introduction
Bienvenue dans **Enter the Matrix**, une série d'exercices sur l'algèbre linéaire en Python. Ce projet vise à comprendre et manipuler les vecteurs, les matrices et d'autres concepts mathématiques essentiels en informatique. Si tu n'es pas à l'aise avec les maths, pas de panique ! Chaque exercice est expliqué de manière simple et progressive.

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

### Exercice 00 - Vecteurs et Matrices
- Un **vecteur** est une liste de nombres représentant une direction et une magnitude.
- Une **matrice** est un tableau de nombres disposés en lignes et colonnes.
- En Python, on manipule ces objets avec des **listes imbriquées**.

### Exercice 01 - Combinaison Linéaire
- Une **combinaison linéaire** est une somme pondérée de vecteurs.
- En informatique, elle s’écrit sous forme de boucles et d'opérations sur les listes.

### Exercice 02 - Interpolation Linéaire (LERP)
- L'**interpolation linéaire** (LERP) permet de calculer un point entre deux valeurs.
- En Python, on utilise une simple **formule mathématique** :
  ```python
  lerp(a, b, t) = a + (b - a) * t
  ```

### Exercice 03 - Produit Scalaire
- Le **produit scalaire** mesure la similarité entre deux vecteurs.
- En Python, il se calcule avec une **somme des produits élémentaires**.

### Exercice 04 - Norme d’un Vecteur
- La **norme** d'un vecteur est sa longueur.
- Elle se calcule avec la **racine carrée de la somme des carrés**.
  ```python
  norm = sqrt(x1**2 + x2**2 + ... + xn**2)
  ```

### Exercice 05 - Cosinus de l’Angle entre deux Vecteurs
- On peut mesurer l'angle entre deux vecteurs avec le **cosinus**.
- Formule :
  ```python
  cos_theta = dot_product(v1, v2) / (norm(v1) * norm(v2))
  ```

### Exercice 06 - Produit Vectoriel
- Le **produit vectoriel** donne un vecteur perpendiculaire aux deux autres.
- En 3D, il se calcule avec la matrice suivante :
  ```python
  cross_product = [y1*z2 - y2*z1, z1*x2 - z2*x1, x1*y2 - x2*y1]
  ```

### Exercice 07 - Matrices et Transformations
- Une **matrice** est utilisée pour effectuer des transformations (rotation, mise à l'échelle).
- On peut appliquer une matrice à un vecteur en multipliant **chaque ligne** par le vecteur.

### Exercice 08 - Multiplication Matrice-Matrice
- Multiplier deux matrices consiste à calculer chaque **élément de la nouvelle matrice** en faisant le produit des lignes et colonnes correspondantes.

### Exercice 09 - Matrices Carrées et Identité
- Une **matrice carrée** a le même nombre de lignes et colonnes.
- Une **matrice identité** est une matrice avec des `1` sur la diagonale et des `0` ailleurs.

### Exercice 10 - Trace d’une Matrice
- La **trace** d'une matrice est la somme des éléments sur sa diagonale principale.
- C'est utile pour certaines transformations linéaires.

### Exercice 11 - Matrice Transposée
- Une **transposée** échange les lignes et les colonnes d'une matrice.
- En Python, on peut l'obtenir avec :
  ```python
  transpose = list(zip(*matrix))
  ```

### Exercice 12 - Matrice Échelonnée
- Une **matrice échelonnée** simplifie les calculs en la mettant sous forme triangulaire.
- Cela aide à résoudre des systèmes d'équations.

### Exercice 13 - Déterminant d’une Matrice
- Le **déterminant** d’une matrice est un **nombre** indiquant si elle est inversible.
- Il se calcule récursivement en réduisant la matrice.

### Exercice 14 - Génération de Projet 3D
- Cet exercice applique les concepts aux **transformations 3D**.
- Pour générer un fichier `.proj`, utilise :
  ```sh
  python3 -m ex14.generate_proj
  ```
- Pour afficher le projet, exécute :
  ```sh
  ./display
  ```

### Exercice 15 - Nombres Complexes
- Les **nombres complexes** ont une partie réelle et imaginaire.
- Ils s’écrivent sous la forme `a + bi`.
- Les matrices de nombres complexes sont utiles pour la physique quantique et la modélisation mathématique.
- En Python, on peut utiliser :
  ```python
  complex_matrix = [[complex(1, 2), complex(3, -1)], [complex(-2, 4), complex(0, 3)]]
  ```

---

## Conclusion
Ce projet permet de **comprendre l'algèbre linéaire par la pratique** en Python. Chaque exercice introduit une nouvelle notion avec des **applications concrètes**.

