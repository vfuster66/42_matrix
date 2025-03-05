# Exercice 02 - Interpolation Linéaire (LERP)

## Introduction
L’**interpolation linéaire** (Linear Interpolation, ou **LERP**) est une méthode permettant de **trouver une valeur intermédiaire** entre deux points. C'est un concept clé en **informatique graphique**, en **animation**, en **traitement du signal** et en **apprentissage automatique**.

Dans cet exercice, nous allons voir comment l’interpolation linéaire fonctionne et comment elle est utilisée en programmation.

---

## Explication Mathématique

L’interpolation linéaire entre deux points \( a \) et \( b \) est définie par la formule suivante :

\[
LERP(a, b, t) = a + (b - a) \times t
\]

Où :
- \( a \) est le premier point,
- \( b \) est le second point,
- \( t \) est un paramètre compris entre \( 0 \) et \( 1 \) qui indique la position relative entre \( a \) et \( b \).

Quelques valeurs caractéristiques :
- Si \( t = 0 \), alors \( LERP(a, b, t) = a \) (début de l’intervalle).
- Si \( t = 1 \), alors \( LERP(a, b, t) = b \) (fin de l’intervalle).
- Si \( t = 0.5 \), alors \( LERP(a, b, t) \) est le **point médian** entre \( a \) et \( b \).

Exemple :
\[
LERP(2, 10, 0.5) = 2 + (10 - 2) \times 0.5 = 6
\]

L’interpolation linéaire peut être étendue à des **vecteurs** en appliquant la formule à chaque composante :

\[
LERP(v_1, v_2, t) = v_1 + (v_2 - v_1) \times t
\]

---

## Implémentation en Python

L’implémentation en Python est simple et suit directement la formule mathématique.

### Interpolation sur des scalaires :
```python
def lerp(a: float, b: float, t: float) -> float:
    """
    Calcule l'interpolation linéaire entre a et b en fonction de t.
    """
    return a + (b - a) * t

# Exemple d'utilisation
print(lerp(2, 10, 0.5))  # Output: 6.0
```

### Interpolation sur des vecteurs avec NumPy :
```python
import numpy as np

def lerp_vector(v1: np.ndarray, v2: np.ndarray, t: float) -> np.ndarray:
    """
    Calcule l'interpolation linéaire entre deux vecteurs.
    """
    return v1 + (v2 - v1) * t

# Exemple d'utilisation
v1 = np.array([1, 2])
v2 = np.array([3, 4])
t = 0.5
print(lerp_vector(v1, v2, t))  # Output: [2. 3.]
```

L’avantage d’utiliser **NumPy** est que cette approche fonctionne pour **n’importe quelle dimension de vecteurs**.

---

## Applications en Informatique

### 1. **Graphisme et Animation** 🎨
- Utilisé pour **animer des objets** entre deux positions.
- Permet de **générer des transitions fluides**.
- Utilisé en **color blending** (mélange de couleurs).

### 2. **Jeux Vidéo** 🎮
- LERP est utilisé pour **mouvements progressifs** entre des points.
- Exemples : déplacement d’un personnage, interpolation de caméra.

### 3. **Traitement du Signal et Son** 🎵
- Utilisé pour **lissage de données** et **transition progressive entre échantillons**.

### 4. **Machine Learning et Régressions** 📊
- Utilisé en **régression linéaire** pour **prédire une valeur intermédiaire**.

---

## Conclusion
L’interpolation linéaire est un outil essentiel qui permet de **créer des transitions fluides** en informatique. Elle est **simple mais puissante**, et largement utilisée dans **divers domaines** allant des **jeux vidéo** au **machine learning**. Cet exercice nous permet de bien comprendre comment interpoler entre deux points, que ce soit **des nombres ou des vecteurs**.

---

## Sources et Références
- [Math for Programmers - Amit Patel](https://amitness.com/posts/math-for-programmers)
- [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [3Blue1Brown - Linear Algebra Playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDOjMrKFR2z6lUO3N58ay1-)