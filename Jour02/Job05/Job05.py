num1 = 1
num2 = 2
operator = "+"
def calcule(num1, operator, num2):
    if operator == '+':
        return  num1 + num2
    elif operator == '-':
        return  num1 - num2
    elif operator =="*":
        return  num1 * num2
    elif operator =="/":
        return  num1 % num2
    else :
        print("Opérateur invalide")

print(calcule(num1, operator, num2))
print(calcule(10, "-", 2))
print(calcule(4, "*", 20))
print(calcule(15, "/", 3))
print(calcule(11, "%", 3))

