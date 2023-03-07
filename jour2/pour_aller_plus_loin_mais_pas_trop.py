from math import *
def longueurs(a, b, c):
    if a == b and a != c or a == c and a != b:
        print("cest un triangle isocèle.")
    elif a == b and b == c:
        print("C'est un triagle equilateral")
    elif a * a + b * b == c * c:
        print("C'est un triagle rectangle")
    else:
        print("C'est un triagle quelquonque")

valeur1 = int(input("Entré une premiere valeur entière: "))
valeur2 = int(input("Entré une seconde valeur entière: "))
valeur3 = int(input("Entré une troisième valeur entière: "))

longueurs(valeur1,valeur2,valeur3)
