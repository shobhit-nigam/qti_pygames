class Bank:
    custId = 0
    name = "john doe"
    opening_bal = 0
    current_bal = 0

    def setData(self, id, n, ob):
        self.custId = id
        self.name = n
        self.opening_bal = self.current_bal = ob

    def display(self):
        print(f"welcome {self.name}, your current balance is {self.current_bal}")

obja = Bank()
objb = Bank()
obja.setData(456800, "dead pool", 1500)
objb.setData(456802, "wolverine", 1800)

obja.display()
