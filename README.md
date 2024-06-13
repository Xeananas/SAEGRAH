# Projet de Manipulation de Graphes avec NetworkX

Ce projet utilise la bibliothèque NetworkX pour manipuler des graphes représentant des acteurs et leurs collaborations. Il inclut également des fonctions pour lire des données JSON et les convertir en graphes, et pour effectuer diverses analyses sur ces graphes.

## Prérequis

Assurez-vous d'avoir installé les bibliothèques suivantes :
- NetworkX
- Matplotlib
- SciPy

Vous pouvez les installer en utilisant pip :
```sh
pip install networkx matplotlib scipy
```
### Menu Interactif

Le script propose les options suivantes :

- **Collaborateurs communs** : Trouve les acteurs communs entre deux acteurs donnés.

- **Collaborateurs proches** : Affiche les collaborateurs proches d'un acteur jusqu'à une distance `k`.

- **Distance entre acteurs** : Calcule la distance entre deux acteurs dans le graphe.

- **Acteur le plus central** : Trouve l'acteur le plus central dans le graphe.

- **Distance maximale entre acteurs** : Calcule la distance maximale entre tous les acteurs du graphe.

- **Centre de groupe d'acteurs** : Trouve l'acteur qui est le centre d'un groupe d'acteurs donné.

- **Convertir le fichier TXT en JSON** : Convertit un fichier texte contenant des objets JSON en un fichier JSON.

- **Convertir le fichier JSON en graphe** : Charge un fichier JSON et le convertit en un graphe NetworkX.

- **Afficher le graphe** : Affiche le graphe actuel.

- **Quitter** : Quitte le programme.


#### Exemple d'utilisation

- **Collaborateurs communs**
    - Saisissez `1` pour sélectionner cette option.
    - Entrez le nom des deux acteurs pour lesquels vous voulez trouver les collaborateurs communs.

- **Collaborateurs proches**
    - Saisissez `2` pour sélectionner cette option.
    - Entrez le nom de l'acteur et la distance `k` pour afficher les collaborateurs proches.

- **Distance entre acteurs**
    - Saisissez `3` pour sélectionner cette option.
    - Entrez le nom des deux acteurs pour calculer la distance entre eux.

- **Acteur le plus central**
    - Saisissez `4` pour sélectionner cette option.
    - Le script affichera l'acteur le plus central du graphe.

- **Distance maximale entre acteurs**
    - Saisissez `5` pour sélectionner cette option.
    - Le script affichera la distance maximale entre tous les acteurs du graphe.

- **Centre de groupe d'acteurs**
    - Saisissez `6` pour sélectionner cette option.
    - Le script affichera l'acteur qui est le centre d'un groupe d'acteurs donné.

- **Convertir le fichier TXT en JSON**
    - Saisissez `7` pour sélectionner cette option.
    - Entrez le nom du fichier texte à convertir.

- **Convertir le fichier JSON en graphe**
    - Saisissez `8` pour sélectionner cette option.
    - Entrez le nom du fichier JSON à convertir.

- **Afficher le graphe**
    - Saisissez `9` pour sélectionner cette option.
    - Le graphe sera affiché à l'écran.

- **Quitter**
    - Saisissez `10` pour quitter le programme.
