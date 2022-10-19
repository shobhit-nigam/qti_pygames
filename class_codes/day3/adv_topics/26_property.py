class Currency:
    def __init__(self, amount=0):
        self.amount = amount

    def to_rupee(self):
        return self.amount * 82.7

    def get_amount(self):
        return self.__amount

    def set_amount(self, val):
        if val > 1000:
            raise ValueError("maximum conversion reached")
        self.__amount = val

    amount = property(get_amount, set_amount)


obja = Currency(100)
print(obja.amount)
print(obja.to_rupee())
'''
obja.amount = 200
print(obja.to_rupee())

obja.amount = 2000
print(obja.amount)
print(obja.to_rupee())
'''
