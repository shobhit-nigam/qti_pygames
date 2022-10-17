class Bank:
    custId = 0
    name = "john doe"
    opening_bal = 0
    current_bal = 0

    def display(self):
        print(f"welcome {self.name}, your current balance is {self.current_bal}")

obja = Bank()
objb = Bank()

obja.current_bal = 1500
obja.name = "dead pool"
objb.name = "wolverine"
obja.grade = "A"

print(obja.grade)
# error
print(Bank.grade)
print(objb.grade)
