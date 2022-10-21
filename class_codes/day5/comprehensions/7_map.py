lista = [11, 13, 6, 8, 4, 19, 4, 20, 7]
listb = [14, 18, 4, 2, 7, 16, 9, 17, 3, 5, 8, 11]

def funcx(la, lb):
    return la*2 + lb - 4

listc = []

if len(lista) < len(listb):
    for i in range(len(lista)):
        listc.append(funcx(lista[i], listb[i]))
else:
    for i in range(len(listb)):
        listc.append(funcx(lista[i], listb[i]))

print(listc)   
