class Bank:
    custId = 0
    name = "john doe"
    opening_bal = 0
    current_bal = 0

    def display(ttt):
        print(f"welcome {ttt.name}, your current balance is {ttt.current_bal}")

obja = Bank()
objb = Bank()

obja.display()
# obja.display() --> Bank.display(obja)

objb.display()
# objb.display() --> Bank.display(objb)

obja.current_bal = 1500
obja.name = "dead pool"
objb.name = "wolverine"

print("-"*10)

obja.display()
objb.display()
