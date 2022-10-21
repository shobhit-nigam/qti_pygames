lista = [11, 13, 6, 8, 4, 19, 4, 20, 7]
listb = [14, 18, 4, 2, 7, 16, 9, 17, 3]

listnew = [x for x in range(1, 101) if x%3 == 0 or x%5 == 0]

listnew = ["yes" if x%3 == 0 or x%5 == 0 else "no" for x in range(1, 11)]

print(listnew)
