import time
import requete

requete.graph = None
def menu():
    print("Menu:")
    print("1. Collaborateurs communs")
    print("2. Collaborateurs proches")
    print("3. Distance entre acteurs")
    print("4. Acteur le plus central")
    print("5. Distance maximale entre acteurs")
    print("6. Centre de groupe d'acteurs")
    print("7. Convertir le fichier txt en json")
    print("8. Convertir le fichier json en graphe")
    print("9. Quitter")

def choix():
    choix = input("Entre ton choix: ")
    return choix

def action(choix):
    if choix == "1":
        act1 = input("Entre le premier acteur: ")
        act2 = input("Entre le deuxième acteur: ")
        requete.collaborateurs_communs(requete.graph, act1, act2)
    
    elif choix == "2":
        act = input("Entre le nom de l'acteur: ")
        k = int(input("Entre la distance k: "))
        requete.collaborateurs_proches(requete.graph, act, k)

    elif choix == "3":
        act1 = input("Entre le premier acteur: ")
        act2 = input("Entre le deuxième acteur: ")
        print(requete.distance_acteurs(requete.graph, act1, act2))

    elif choix == "4":
        acteur_central = requete.acteur_plus_central(requete.graph)
        print("L'acteur le plus central est: ", acteur_central)
    
    elif choix == "5":
        print(requete.distance_max_acteurs(requete.graph))

    
    elif choix == "6":
        print(requete.centre_groupe_acteurs(requete.graph))

    elif choix == "7":
        data = input("Entre le nom du fichier txt: ")
        requete.txt_to_json(data, "data.json")
        print("Conversion du fichier txt en json...")
        print("Conversion terminée!")
    elif choix == "8":
        data = input("Entre le nom du fichier json: ")
        requete.json_vers_nx(data)
        print("Conversion du fichier json en graphe...")
        requete.graph = requete.json_vers_nx(data)
        print("Conversion terminée!")

    elif choix == "9":
        print("Au revoir!")
    else:
        print("Mauvais choix!")


while True:

    menu()
    user_choix = choix()
    action(user_choix)
    if user_choix == "9":
        break
    time.sleep(5)