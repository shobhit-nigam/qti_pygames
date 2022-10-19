def stars(gen):
    def inner(data):
        print("**********")
        gen(data)
        print("**********")
    return inner

def hashes(gen):
    def inner(data):
        print("##########")
        gen(data)
        print("##########")
    return inner

@stars
@hashes
def display(message):
    print(message)


display("valar morghulis")
