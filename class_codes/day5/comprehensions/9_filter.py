lista = [11, 13, 6, 8, 4, 19, 4, 20, 7]
listb = [14, 18, 4, 2, 7, 16, 9, 17, 3, 5, 8, 11]

vowels = ['a', 'e', 'i', 'o', 'u']

listx = list(filter(lambda x : x in vowels , "may the force be with you"))

print(listx)
