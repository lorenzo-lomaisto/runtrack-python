def calcule(num1, operator, num2):
    result = 0
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator =="*":
        result = num1 * num2
    elif operator =="/":
        result = num1 % num2
    else :
        print("Opérateur invalide")
        return result
print(calcule(5, "+", 10))
print(calcule(10, "-", 2))
print(calcule(4, "*", 20))
print(calcule(15, "/", 3))
print(calcule(11, "%", 3))

