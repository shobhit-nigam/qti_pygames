class Cricket:
    def __init__(self, o=0, b=0):
        self.overs = o
        self.balls = b

    def display(self):
        print(f"{self.overs} overs and {self.balls} balls bowled")

    def __add__(self, other):
        objt = Cricket()
        temp_balls = self.overs * 6 + self.balls + other.overs *6 + other.balls
        objt.overs = temp_balls//6
        objt.balls = temp_balls%6
        return objt


obja = Cricket(6, 4)
objb = Cricket(3, 5)

obja.display()
    # Cricket.display(obja)

total = obja + objb
    # obja.__add__(objb)
    # Cricket.__add__(obja, objb)

total.display()
