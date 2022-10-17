class Bank:

    def __init__(self, id, n, ob):
        self.custId = id
        self.name = n
        self.opening_bal = self.current_bal = ob
        return None

    def display(self):
        print(f"welcome {self.name}, your current balance is {self.current_bal}")

obja = Bank(456800, "dead pool", 1500)
objb = Bank(456802, "wolverine", 1800)

obja.display()
objb.display()

x = obja.__init__(456800, "alive pool", 2000)
obja.display()

print("return value of __init__", x)
