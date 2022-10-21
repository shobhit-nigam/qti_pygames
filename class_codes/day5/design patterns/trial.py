class Sample:
    data = 10
    datb = 20

    def calc(self):
        la = self.data * 2 + self.datb * 2
        return la

    def funca(self):
        self.datc = 100

objs = Sample()

print(objs.calc())

def linear(self, val):
    la = self.data + self.datb + val
    return la

Sample.calc = linear
objt = Sample()
print(objt.calc(100))
