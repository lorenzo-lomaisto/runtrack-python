L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

min_element = L[0] 
max_element = L[0]

for i in L:
    if i < min_element:
        min_element = i
    elif i > max_element:
        max_element = i

print("Le minimum des éléments de la liste L est :", min_element)
print("Le maximum des éléments de la liste L est :", max_element)