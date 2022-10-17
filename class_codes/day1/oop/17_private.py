class Bank:
    team = "marvel"

    def __init__(self, id, n, ob):
        self.custId = id
        self.name = n
        self.opening_bal = self.current_bal = ob
        self.check_grade()
        return None

    def check_grade(self):
        if self.opening_bal < 200:
            self.__grade = "E"
        elif 200 <= self.opening_bal < 800:
            self.__grade = "D"
        elif 800 <= self.opening_bal < 1600:
            self.__grade = "C"
        elif 1600 <= self.opening_bal < 2500:
            self.__grade = "B"
        else :
            self.__grade = "A"

    def loan_eligibility(self):
        if self.__grade == "B":
            self.__loan = self.current_bal * 4
        elif self.__grade == "C":
            self.__loan = self.current_bal * 3.5
        elif self.__grade == "D":
            self.loan = self.current_bal * 2.5
        elif self.__grade == "E":
            self.__loan = self.current_bal * 1.5
        else:
            self.__loan = 0

        print(f"Mr. {self.name} you are eligible for a loan of {int(self.__loan)}")


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
            print(f"Mr. {self.name}you do not have enough balance")

obja = Bank(456800, "dead pool", 1500)
objb = Bank(456802, "wolverine", 1800)

obja.deposit(300)
print("____________")
obja.loan_eligibility()
print("____________")
objb.loan_eligibility()
print("____________")

# error
print(f"grade of obja.name = {obja.__grade}")
obja.loan_eligibility()
