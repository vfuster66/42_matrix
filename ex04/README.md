# Exercice 04 - Norme d'un Vecteur

## Introduction
Dans cet exercice, nous allons explorer la notion de **norme d'un vecteur** en algèbre linéaire. La norme permet de mesurer la longueur ou la magnitude d'un vecteur, ce qui est essentiel en physique, en machine learning, en informatique graphique et bien d'autres domaines.

---

## Concept Mathématique
La **norme d'un vecteur** est une mesure de sa longueur dans l'espace. Il existe plusieurs types de normes, mais nous nous intéresserons ici principalement à :

1. **Norme Euclidienne (norme 2)** :
   Elle est définie par la formule suivante :
   \[
   \| \mathbf{v} \|_2 = \sqrt{v_1^2 + v_2^2 + ... + v_n^2}
   \]
   Cela correspond au théorème de Pythagore généralisé en plusieurs dimensions.

2. **Norme 1 (ou norme de Manhattan)** :
   \[
   \| \mathbf{v} \|_1 = |v_1| + |v_2| + ... + |v_n|
   \]
   Elle correspond à la distance parcourue si l'on ne peut se déplacer que selon les axes.

3. **Norme infinie (ou norme max)** :
   \[
   \| \mathbf{v} \|_\infty = \max ( |v_1|, |v_2|, ..., |v_n| )
   \]
   Elle correspond à la plus grande valeur absolue des composantes du vecteur.

---

## Traduction en Informatique
En Python, ces normes peuvent être calculées de différentes manières.

### Norme Euclidienne
Sans utiliser de bibliothèque externe :
```python
import math

def norm_euclidean(vector):
    return math.sqrt(sum(x**2 for x in vector))
```
Avec **NumPy** :
```python
import numpy as np

def norm_euclidean(vector):
    return np.linalg.norm(vector, ord=2)
```

### Norme de Manhattan
```python
def norm_manhattan(vector):
    return sum(abs(x) for x in vector)
```

### Norme infinie
```python
def norm_inf(vector):
    return max(abs(x) for x in vector)
```

---

## Application
La norme d'un vecteur est essentielle dans plusieurs domaines :
- **En physique** : pour calculer des distances et des forces.
- **En machine learning** : la norme est utilisée dans la régularisation des modèles (L1 et L2 regularization).
- **En informatique graphique** : pour normaliser des vecteurs afin de définir des directions de lumière.
- **En calcul scientifique** : pour mesurer la différence entre des vecteurs en analyse de données.

---

## Instructions pour l'exercice
Dans cet exercice, tu dois implémenter les différentes normes d'un vecteur et tester leur fonctionnement avec plusieurs vecteurs.



