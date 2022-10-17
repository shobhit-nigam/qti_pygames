class Bank:
    team = "marvel"

    def __init__(self, id, n, ob):
        self.custId = id
        self.name = n
        self.opening_bal = self.current_bal = ob
        return None

    def display(self):
        print(f"welcome {self.name}, your current balance is {self.current_bal}")

    def deposit(self, amt):
        self.current_bal = self.current_bal + amt
        print(f"thank you {self.name}, your deposit is successfull")

    def withdraw(self, amt):
        if self.current_bal > amt:
            self.current_bal = self.current_bal - amt
            print(f"thank you {self.name}, your withdrawal is successfull")
        else:
            print(f"you do not have enough balance")

obja = Bank(456800, "dead pool", 1500)
objb = Bank(456802, "wolverine", 1800)

obja.withdraw(2000)
print("____________")
obja.deposit(1600)
obja.withdraw(2000)
print("____________")
obja.display()
