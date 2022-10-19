def funca():
    print("in a")
    def funcb():
        print("in b")
        return 100
    x = funcb()
    print("in a, ret val of b is", x)
    return x

y = funca()
print("y =", y)
