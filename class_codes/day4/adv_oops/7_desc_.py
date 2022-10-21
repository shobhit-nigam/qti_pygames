class SampleA:
    data_a = "some data of a"
    def __init__(self):
        self.var_a = "instance attribute of a"

class SampleB(SampleA):
    data_b = "some data of b"
    def __init__(self):
        super().__init__()
        self.var_b = "instance attribute of b"

objb = SampleB()

print(objb.data_a)
print(objb.var_a)
print(objb.data_b)
print(objb.var_b)

# error

print(objb.var_c)
