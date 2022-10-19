class Cricket:
    def __init__(self, o=0, b=0):
        self.overs = o
        self.balls = b

    def display(self):
        print(f"{self.overs} overs and {self.balls} balls bowled")

    def __add__(self, other):
        if type(other) is Cricket:
            objt = Cricket()
            temp_balls = self.overs * 6 + self.balls + other.overs *6 + other.balls
            objt.overs = temp_balls//6
            objt.balls = temp_balls%6
            return objt

        elif type(other) is int:
            objt = Cricket()
            temp_balls = self.overs * 6 + self.balls + other
            objt.overs = temp_balls//6
            objt.balls = temp_balls%6
            return objt

    def __lt__(self, other):
        return (self.overs*6 + self.balls) < (other.overs*6 + other.balls)


obja = Cricket(6, 4)
objb = Cricket(3, 5)
objc = Cricket(1, 4)

total = obja + objb + objc
    # obja.__add__(objb)
    # Cricket.__add__(obja, objb)
total.display()

total = total + 1

total.display()

print(obja < objb)
