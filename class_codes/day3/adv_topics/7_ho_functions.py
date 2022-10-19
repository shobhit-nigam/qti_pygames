def bake(food):
    print(f"bake {food}")

def fry(food):
    print(f"fry {food}")

#bake("cookies")
#fry("papad")

def cook(gen, food):
    gen(food)
    # bake("cake")

cook(bake, "cake")
