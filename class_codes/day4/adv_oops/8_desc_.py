class SampleA:

    def __init__(self, initval=None):
        print("init of a")
        self.__set__(self, initval)

    def __get__(self, instance, obj):
        print(instance, obj)
        print(f"getting val = {self.val}")
        return self.val

    def __set__(self, instance, val):
        print(f"setting self.val to {val}")
        self.val = val

class SampleB:
    x = SampleA("hello")

objb = SampleB()
print("-------")
print(objb.x)
objb.x = "namaste"
print("-------")
print(objb.x)
