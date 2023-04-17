L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
somme_paires = 0

for i in L:
    if i % 2 == 0:
        somme_paires += i

print("La somme des valeurs paires de la liste L est :", somme_paires)