def distance_toilettes(marches, hauteur):
    distance_jour = marches * hauteur * 2 # distance parcourue en montant et descendant une fois
    distance_semaine = distance_jour * 5 * 7 # distance parcourue en une semaine (5 fois par jour, 7 jours par semaine)
    distance_m = distance_semaine / 100 # conversion en mètres
    return distance_m

# Exemple d'utilisation de la fonction
x = 100 # nombre de marches
y = 20 # hauteur de chaque marche en cm
distance = distance_toilettes(x, y)
print(f"Pour {x} marches de {y} cm, le gardien parcours {distance:.2f} m par semaine.")
    


