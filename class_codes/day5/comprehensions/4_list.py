listx = [['aa', 'bb'],
        ['ff', 'rr'],
        ['ll', 'bb'],
        ['ee', 'dd']]

print(listx)

listy = [[row[i] for row in listx] for i in range(2)]
print(listy)
