class Bank:
    custId = 0
    name = "john doe"
    opening_bal = 0
    current_bal = 0

    def display():
        print("hello")
        # print(f"welcome {name}, your current balance is {current_bal}")

obja = Bank()
objb = Bank()
# error 
obja.display()
print("-"*10)
obja.custId = 648932
