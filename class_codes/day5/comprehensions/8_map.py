lista = [11, 13, 6, 8, 4, 19, 4, 20, 7]
listb = [14, 18, 4, 2, 7, 16, 9, 17, 3, 5, 8, 11]

listc = list(map(lambda la, lb: la*2 + lb - 4, lista, listb))

print(listc)
