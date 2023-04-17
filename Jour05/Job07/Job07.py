def change_word(word):
    # Vérification que le mot contient uniquement des lettres de l'alphabet
    if not word.isalpha():
        return "Le mot doit contenir uniquement des lettres de l'alphabet."
    
    # Conversion du mot en une liste de caractères
    chars = list(word)
    
    # Parcours de la liste à partir de la fin pour trouver les deux lettres à échanger
    for i in range(len(chars) - 1, 0, -1):
        if chars[i] > chars[i-1]:
            # Recherche de la plus petite lettre plus grande que chars[i-1] dans la fin de la liste
            smallest = i
            for j in range(i, len(chars)):
                if chars[j] > chars[i-1] and chars[j] < chars[smallest]:
                    smallest = j
            
            # Échange des deux lettres
            chars[i-1], chars[smallest] = chars[smallest], chars[i-1]
            
            # Tri des lettres après i-1 dans l'ordre croissant
            chars[i:] = sorted(chars[i:])
            
            # Reconstitution du mot à partir de la liste de caractères et renvoi
            return ''.join(chars)
    
    # Si aucune paire de lettres n'a pu être échangée, cela signifie que le mot est déjà le dernier dans l'ordre alphabétique
    return "Le mot est déjà le dernier dans l'ordre alphabétique."

# Exemple d'utilisation
word = input("Entrez un mot sans espace ni caractère spécial : ")
new_word = change_word(word)
print(f"Le mot suivant dans l'ordre alphabétique est : {new_word}")