def hashes(gen):
    def inner(data):
        print("##########")
        gen(data)
        print("##########")
    return inner

@hashes
def display(message):
    print(message)




display("valar morghulis")
