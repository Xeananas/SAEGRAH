import json
import networkx as nx
import matplotlib.pyplot as plt
import scipy.sparse



import json
import networkx as nx
import matplotlib.pyplot as plt

def txt_to_json(input_file, output_file):
    """
    Lit un fichier texte contenant des objets JSON sur chaque ligne et les écrit dans un nouveau fichier JSON.

    Args:
        input_file (str): Nom du fichier texte d'entrée contenant les chaînes JSON.
        output_file (str): Nom du fichier de sortie pour écrire le tableau JSON.
    """
    try:
        json_list = []
        with open(input_file, 'r') as file:
            for line in file:
                #Convertir la chaîne JSON en un dictionnaire Python et l'ajouter à la liste
                json_obj = json.loads(line)
                json_list.append(json_obj)

        #Écrire la liste des objets JSON dans le fichier de sortie
        with open(output_file, 'w') as file1:
            json.dump(json_list, file1, indent=4)

        print("Les données ont été écrites avec succès dans " + output_file)

    except Exception as e:
        print("Il y a une erreur !")

txt_to_json('data_100.txt', 'data_100.json')


def json_vers_nx(chemin): #Q1

    with open(chemin, 'r') as f:
        donnees = json.load(f)

    #On initialise le graphe avec le nom Gc
    G = nx.Graph()

    #Pour chaque film dans le fichier json
    for film in donnees:
        for actor in film['cast']:
            actor_name = actor.replace('[[', '').replace(']]', '').split('|')[-1]#nom acteur 
            G.add_node(actor_name)#création du noeud
            
            for acteur in film["cast"]:
                acteur_nom = acteur.replace('[[', '').replace(']]', '').split('|')[-1]
                if actor_name != acteur_nom:
                    G.add_edge(actor_name,acteur_nom)
            
            


    return G
graph = json_vers_nx('data_100.json')
plt.clf()

#nx.draw(graph, with_labels=True)
#plt.show()

def collaborateurs_communs(G,u,v): #Q2
    
  
    act1 = set(G.neighbors(u))
    act2 = set(G.neighbors(v))
    communs = act1.intersection(act2)
    if len(communs) == 0:
        return "aucun acteur sont en commun!"
    return print("les acteurs communs sont : " ,communs)

# acteurs_communs(graph,"Peter Kowanko","Al Pacino")






def collaborateurs_proches(G,u,k): #Q3
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    print(collaborateurs)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs



def distance_acteurs(G, act1, act2):
    distance = 0
    while act2 not in collaborateurs_proches(G, act1, distance):
        distance += 1
    return distance

def centralite(G, acteur):
    distance_max = 0
    for autre_acteur in G.nodes:
        if acteur != autre_acteur:
            distance = distance_acteurs(G, acteur, autre_acteur)
            if distance > distance_max:
                distance_max = distance
    return distance_max

def acteur_plus_central(G):
    acteur_central = None
    centralite_max = 0
    for acteur in G.nodes:
        centralite_acteur = centralite(G, acteur)
        if centralite_acteur > centralite_max:
            centralite_max = centralite_acteur
            acteur_central = acteur
    return acteur_central




def distance_max_acteurs(G):
    distance_max = 0
    for acteur1 in G.nodes:
        for acteur2 in G.nodes:
            if acteur1 != acteur2:
                distance = distance_acteurs(G, acteur1, acteur2)
                if distance > distance_max:
                    distance_max = distance
    return distance_max
print(distance_max_acteurs(graph))

def centre_groupe_acteurs(G, groupe):
    centre = None
    distance_min = float('inf')
    for acteur in G.nodes:
        distance_totale = 0
        for membre in groupe:
            distance = distance_acteurs(G, acteur, membre)
            distance_totale += distance
        if distance_totale < distance_min:
            distance_min = distance_totale
            centre = acteur
    return centre

 