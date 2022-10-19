class Cricket:
    def __init__(self, o=0, b=0):
        self.overs = o
        self.balls = b

    def __repr__(self):
        return f"Cricket({self.overs} ,{self.balls})"

    def __str__(self):
        return f"{self.overs} overs and {self.balls} balls"

    def __call__(self):
        print(f"{self.overs} overs and {self.balls} balls")


obja = Cricket(6, 4)
objb = Cricket(3, 5)

obja()
