class Bank:

    def __init__(self, id, n, ob):
        self.custId = id
        self.name = n
        self.opening_bal = self.current_bal = ob

    def display(self):
        print(f"welcome {self.name}, your current balance is {self.current_bal}")

obja = Bank(456800, "dead pool", 1500)
objb = Bank(456802, "wolverine", 1800)

obja.display()
objb.display()
