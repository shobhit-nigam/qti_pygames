def funca():
    print("plain home")


def funcb(gen):
    def funcc():
        gen()
        print("decorated home")
    return funcc

funca()
print("-"*10)

funcx = funcb(funca)
        # = return value of funcb
        # = funcc

funcx()
