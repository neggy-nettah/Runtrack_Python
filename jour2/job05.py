
def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        print("Erreur veuillez réessayer.")
    
num1 = int(input("Entrez un nombre. "))
operator = input("Entrez un opérateur. ")
num2 = int(input("Entrez un nombre. "))


print(calcule(num1, operator, num2))

