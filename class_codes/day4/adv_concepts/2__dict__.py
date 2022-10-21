class BreakFast:
    def __init__(self, dish, quantity):
        self.dish = dish
        self.quantity = quantity

    def heat(self):
        if self.dish == 'idli':
            return True
        else:
            return False


item_a = BreakFast('dosa', 2)

print(item_a.__dict__)

stra = "hello world"

# error

print(stra.__dict__)
