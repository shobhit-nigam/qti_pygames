def funcb(gen):
    def funcc():
        gen()
        print("decorated home")
    return funcc

@funcb
def funca():
    print("plain home")

funca()
