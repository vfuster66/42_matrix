# Exercice 05 - Cosinus de l'Angle entre Deux Vecteurs

## Introduction
Dans cet exercice, nous allons apprendre à calculer le **cosinus de l'angle** entre deux vecteurs. Cette mesure est essentielle en géométrie, en physique et en intelligence artificielle pour déterminer la similarité entre deux directions.

---

## 1. Notion Mathématique
Le cosinus de l’angle \( \theta \) entre deux vecteurs \( \mathbf{v_1} \) et \( \mathbf{v_2} \) est défini par la formule :

\[
\cos(\theta) = \frac{\mathbf{v_1} \cdot \mathbf{v_2}}{||\mathbf{v_1}|| \times ||\mathbf{v_2}||}
\]

Où :
- \( \mathbf{v_1} \cdot \mathbf{v_2} \) est le **produit scalaire** des vecteurs \( \mathbf{v_1} \) et \( \mathbf{v_2} \).
- \( ||\mathbf{v_1}|| \) et \( ||\mathbf{v_2}|| \) sont les **normes** (ou longueurs) des vecteurs.
- Le résultat varie entre **-1** (vecteurs opposés) et **1** (vecteurs alignés).

Cette mesure est très utilisée en machine learning pour comparer des directions dans un espace vectoriel.

---

## 2. Traduction en Programmation
En informatique, nous traduisons cette formule en Python en utilisant :
- Une fonction pour **le produit scalaire**.
- Une fonction pour **la norme d’un vecteur**.
- L’application de la formule du cosinus.

Voici une implémentation en Python :

```python
import math

def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

def norm(v):
    return math.sqrt(sum(x**2 for x in v))

def cos_angle(v1, v2):
    return dot_product(v1, v2) / (norm(v1) * norm(v2))

# Exemple d'utilisation
v1 = [1, 2, 3]
v2 = [4, 5, 6]

print(cos_angle(v1, v2))
```

---

## 3. Applications en Informatique
Le cosinus de l’angle entre deux vecteurs est utilisé dans plusieurs domaines :
- **Recherche d’information** : Mesure de similarité entre documents en NLP.
- **Jeux vidéo** : Détection d’angles entre objets.
- **Vision par ordinateur** : Comparaison d’orientations.
- **Machine Learning** : Calcul de distances dans des espaces de features.

---

## 4. Résumé
- La formule du cosinus d’un angle est basée sur le produit scalaire et la norme des vecteurs.
- Elle permet de mesurer la similarité entre deux directions.
- En Python, on peut la calculer avec des fonctions simples.

---

## Sources et Références
- [Math for Programmers - Amit Patel](https://amitness.com/posts/math-for-programmers)
- [Khan Academy - Produit Scalaire](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/dot-cross-products/v/defining-the-dot-product)
- [Wikipedia - Similarité Cosinus](https://fr.wikipedia.org/wiki/Similarit%C3%A9_cosinus)

---
