def fruits_legumes(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine,navet")
    else:
        print("Aucun résultat correspondant")

# Exemples d'appel de la fonction avec différents paramètres
fruits_legumes("fruits", "hiver")
fruits_legumes("fruits", "ete")
fruits_legumes("legume", "hiver")
fruits_legumes("legume", "ete")
fruits_legumes("pomme", "automne")