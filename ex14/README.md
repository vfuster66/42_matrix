# Exercice 14 - Matrice de Projection

## Introduction
Dans cet exercice, nous allons explorer le concept de **matrice de projection**, qui est largement utilisé en **géométrie 3D**, **graphismes informatiques** et **vision par ordinateur**. L'objectif est de comprendre comment transformer des points en trois dimensions (3D) en coordonnées 2D à l'aide d'une projection matricielle.

---

## Concepts Mathématiques

### Projection en 3D
Une **projection** est une transformation linéaire qui permet de représenter un espace de dimension supérieure dans un espace de dimension inférieure. Par exemple, dans le cas des graphismes 3D, nous devons projeter un objet en 3D sur un écran 2D.

### Matrice de Projection
La matrice de projection perspective est définie comme suit :

\[
P = \begin{bmatrix}
    f / aspect & 0 & 0 & 0 \\
    0 & f & 0 & 0 \\
    0 & 0 & (z_{far} + z_{near}) / (z_{near} - z_{far}) & (2 z_{far} z_{near}) / (z_{near} - z_{far}) \\
    0 & 0 & -1 & 0
\end{bmatrix}
\]

où :
- **f** est la distance focale,
- **aspect** est le rapport largeur/hauteur de l'écran,
- **z_{near}** et **z_{far}** définissent les plans de découpage proches et lointains.

Cette matrice permet de transformer des coordonnées 3D homogènes en coordonnées normalisées qui peuvent être affichées sur un écran.

---

## Implémentation en Informatique
En Python, nous pouvons représenter une matrice de projection sous forme d'une liste de listes et appliquer une transformation matricielle à un point donné.

Voici une implémentation simple :

```python
import numpy as np

def projection_matrix(f, aspect, z_near, z_far):
    return np.array([
        [f / aspect, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (z_far + z_near) / (z_near - z_far), (2 * z_far * z_near) / (z_near - z_far)],
        [0, 0, -1, 0]
    ])

# Exemple d'utilisation
fov = np.pi / 4  # Champ de vision de 45 degrés
f = 1 / np.tan(fov / 2)
aspect_ratio = 16 / 9
z_near, z_far = 0.1, 100

P = projection_matrix(f, aspect_ratio, z_near, z_far)
print(P)
```

Ce code génère une **matrice de projection perspective** et affiche son contenu.

---

## Utilisation du Logiciel
Un **logiciel est fourni** avec cet exercice pour visualiser l'effet d'une matrice de projection sur des objets 3D. Voici comment l'utiliser :

### Étape 1 : Générer le fichier de projection
Exécutez la commande suivante pour créer un fichier contenant la matrice de projection :
```sh
python3 -m ex14.generate_proj
```

### Étape 2 : Lancer l'affichage
Une fois le fichier généré, utilisez la commande suivante pour afficher la projection en 3D :
```sh
./display
```

Ce programme permet d'afficher un objet projeté à l'aide de la matrice de projection calculée.

Un **README spécifique** est disponible dans le dossier `ex14` pour des détails supplémentaires sur l'utilisation du logiciel.

---

## Applications
- **Graphismes 3D** : conversion de modèles 3D en images affichables sur un écran.
- **Réalité virtuelle et augmentée** : transformation des objets virtuels en perspectives réalistes.
- **Simulation physique** : projection d'objets dans des environnements simulés.

---

## Références
- [Math for Programmers - Amit Patel](https://amitness.com/posts/math-for-programmers)
- [3Blue1Brown - Linear Algebra Playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDOjMrKFR2z6lUO3N58ay1-)
- [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)

---

## Conclusion
Cet exercice montre comment **les transformations linéaires** peuvent être utilisées pour représenter des objets 3D en 2D. La compréhension de la **matrice de projection** est essentielle pour la programmation graphique et les moteurs de rendu 3D.
