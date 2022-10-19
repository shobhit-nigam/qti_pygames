def gen():
    n = 1
    yield n

    n = n + n
    yield n

    n = n + n
    yield n


for val in gen():
    print(val)
