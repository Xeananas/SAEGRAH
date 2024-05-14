import json
import networkx as nx
import matplotlib.pyplot as plt

# Chemin vers le fichier texte
fichier_texte = "data_100.txt"

# Fonction pour lire le fichier texte et convertir chaque ligne en un objet Python
def lire_fichier_texte(chemin):
    donnees = []
    with open(chemin, 'r') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            # Convertir la ligne en objet Python
            objet = json.loads(ligne)
            donnees.append(objet)
    return donnees

# Fonction pour écrire les données au format JSON dans un fichier
def ecrire_json(chemin, donnees_json):
    with open(chemin, 'w') as fichier:
        json.dump(donnees_json, fichier, indent=4)

# Lecture du fichier texte et conversion en liste d'objets Python
donnees = lire_fichier_texte(fichier_texte)

# Écriture des données au format JSON dans un fichier
fichier_json = "caca.json"
ecrire_json(fichier_json, donnees)

print("Conversion réussie. Les données ont été écrites dans le fichier JSON:", fichier_json)


G = nx.Graph()
names = []

with open("donnees2.json", 'r') as json_file:
    data = json.load(json_file)
    for movie in data:
        catch = movie["cast"]
        # Création de liaisons entre les acteurs pour chaque film
        for i in range(len(catch)):
            for j in range(i+1, len(catch)):
                actor1 = catch[i][0].strip("[]")  # Premier acteur
                actor2 = catch[j][0].strip("[]")  # Deuxième acteur
                # Ajout d'une liaison entre les acteurs
                if G.has_edge(actor1, actor2):
                    # Si une liaison existe déjà, on incrémente le poids
                    G[actor1][actor2]['weight'] += 1
                else:
                    # Sinon, on ajoute une nouvelle liaison
                    G.add_edge(actor1, actor2, weight=1)
G.add_edges_from(names)
nx.draw(G, with_labels=True)
plt.show()

