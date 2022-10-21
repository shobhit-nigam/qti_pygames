lista = [11, 13, 6, 8, 4, 19, 4, 20, 7]
listb = [14, 18, 4, 2, 7, 16, 9, 17, 3]

def funcx(la):
    return la%2 == 0

listnew = []

for val in lista:
    if funcx(val):
        listnew.append(val)

print(listnew)
