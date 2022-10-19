rava = 'rava'
choco = 'choco'

def funca(x):
    print(f"making {x} laddoos")

def funcb(x):
    print(f"making {x} barfi")


def make(gen, x):
    gen(x)

make(funca, rava)
make(funcb, choco)
