
def calcule(num1, operator, num2):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "%":
        print(num1 % num2)
    else:
        print("Erreur veuillez réessayer.")
    

calcule(1, "+", 2)
calcule(1, "-", 2)
calcule(1, "*", 2)
calcule(1, "/", 2)
calcule(1, "%", 2)
