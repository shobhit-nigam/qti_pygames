class Dairy:
    def __init__(self,q=0, p=0):
        self.price = p
        self.quantity = q

    def getPrice(self):
        return self.quantity * self.price * 0.9

class Fruits:
    def __init__(self, q=0, p=0):
        self.price = p
        self.quantity = q

    def getPrice(self):
        return self.quantity * self.price

class Eggs:
    def __init__(self, q=0, p=0):
        self.price = p
        self.quantity = q

    def getPrice(self):
        return self.quantity * self.price * 0.8


grocery = [Dairy(3, 60), Fruits(4, 80), Eggs(12, 10)]
total = 0

for item in grocery:
    total = total + item.getPrice()

print(total)
