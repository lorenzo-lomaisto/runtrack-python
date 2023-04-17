def somme_cases_voisines(L):
    L[3] = L[2] + L[4]

L = [1, 2, 3, 4, 5]

print("La valeur de L[1] est :", L[1])

somme_cases_voisines(L)

print("La valeur du dernier terme de la liste est :", L[-1])