
def funca(data):

    def funcb():
        print(data)

    return funcb

funcx = funca("valar dohaeris")

funcx()

del funca

funcx()

# error
funca()
