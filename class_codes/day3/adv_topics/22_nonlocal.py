
def funca():
    a = 10
    print("outside a =", a)
    def funcb():
        a = 100
        print("inside a =", a)
    funcb()
    print("outside a =", a)

funca()
