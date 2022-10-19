def funca():
    print("plain home")


def funcb(gen):
    def funcc():
        gen()
        print("decorated home")
    return funcc

#################
funca()
print("-"*10)
##################

funca = funcb(funca)

funca()
