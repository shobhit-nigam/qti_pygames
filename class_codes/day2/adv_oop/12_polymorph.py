class Cricket:
    def __init__(self, o=0, b=0):
        self.overs = o
        self.balls = b

    def display(self):
        print(f"{self.overs} overs and {self.balls} balls bowled")

obja = Cricket(6, 4)
objb = Cricket(3, 5)

obja.display()

# error
total = obja + objb
total.display()
