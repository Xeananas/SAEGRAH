import json

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
