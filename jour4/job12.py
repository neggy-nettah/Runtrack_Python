
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def ascending_list(L):
    tampon = 0
    i = 0
    for k in L:
        tampon = tampon + 1
    for i in range(tampon) :
        for j in range(i + 1, tampon):
            if L[i] > L[j] :
                L[i], L[j] = L[j], L[i]
    return L

print(ascending_list(L))