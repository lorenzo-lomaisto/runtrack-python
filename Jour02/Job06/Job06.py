def CheckNumber(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("Le nombre est égal à 0")
CheckNumber(5)
CheckNumber(-5)
CheckNumber(0)