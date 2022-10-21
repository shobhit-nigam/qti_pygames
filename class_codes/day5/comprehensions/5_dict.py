listx = [3, 6, 8, 4, 1, 2]

squares = {}
for num in listx:
    squares[num] = num**2

squares = {num:num*num for num in listx}

print(squares)
