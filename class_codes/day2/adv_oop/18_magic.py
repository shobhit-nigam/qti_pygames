class Sample:

    def __init__(self, name):
        print("init is called")
        self.name = name

    def __new__(cls, temp):
        print("__new__ magic method is called")
        instance = object.__new__(cls)
        return instance

hero = Sample("ironman")
