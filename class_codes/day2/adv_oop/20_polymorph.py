class Cricket:
    def __init__(self, o=0, b=0):
        self.overs = o
        self.balls = b

    def __repr__(self):
        return f"Cricket({self.overs} ,{self.balls})"

obja = Cricket(6, 4)
objb = Cricket(3, 5)

print(obja)
