L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
nb_max = 0
nb_min = L[0]
for i in L:
    if i > nb_max :
        nb_max = i
    
    if i < nb_min :
        nb_min = i
    
    
print(nb_max)
print(nb_min)