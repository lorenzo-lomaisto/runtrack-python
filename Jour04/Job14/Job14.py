def my_long_word(n, chaine):
    
    words = chaine.split()
   
    long_words = []
    
    for word in words:
       
        if len(word) > n:
            
            long_words.append(word)
    
    return " ".join(long_words)

chaine = "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"
n = 3
resultat = my_long_word(n, chaine)
print(resultat)