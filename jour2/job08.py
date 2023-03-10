
def fruits_legumes(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "legumes" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legumes" and saison == "été":
        print("artichaut, aubergine,navet")
    else:
        print("Veuillez entrée un type et/ou une saison valide. ")

type = input("Choisissez un type (fruits ou legumes) :")
saison = input("Choisissez une saison (été ou hiver) :")
fruits_legumes(type, saison)