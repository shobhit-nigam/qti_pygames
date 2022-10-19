def funcb(gen):
    def funcc():
        gen()
        print("decorated home")
    return funcc

def funca():
    print("plain home")
funca = funcb(funca)

funca()
