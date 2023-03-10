
L = [10,20,30,20,10,50,60,40,80,50,40]
P = []
for i in L:
    if i not in P:
        P = P + [i]

print(P)

