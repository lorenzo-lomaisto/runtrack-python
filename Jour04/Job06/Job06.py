def echange_premiere_derniere(liste):
    if len(liste) > 0:
        temp = liste[0]
        liste[0] = liste[-1]
        liste[-1] = temp

ma_liste = [1, 2, 3, 4, 5]
print("Ma liste avant l'échange :", ma_liste)
echange_premiere_derniere(ma_liste)
print("Ma liste après l'échange :", ma_liste)