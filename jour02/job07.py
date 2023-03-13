
def choix(language):
    if language == "javascript":
        print("tu es un developpeur web")
    elif language == "python":
        print("tu es un developpeur IA")
    elif language == "java":
        print("tu es un developpeur logiciel")
    elif language == "reactjs":
        print("tu es un developpeur mobile")
    else:
        print("un jour, tu seras le meilleur developpeur...")

question = input("Quel langugage préfère-tu? ")

choix(question)

    