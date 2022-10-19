listx = [11, 22, 33, 44]

obji = iter(listx)

print(next(obji))

print(next(obji))

print(obji.__next__())

print(obji.__next__())

#error
print(next(obji))
