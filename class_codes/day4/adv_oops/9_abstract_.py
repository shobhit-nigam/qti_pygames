from abc import abstractmethod, ABC

class SampleA(ABC):
    def __init__(self, initval=None):
        print("init of a")
        self.val = initval
        super().__init__()

    def method_a(self):
        pass

    @abstractmethod
    def method_b(self):
        print("love indian food")
        pass


class SampleB(SampleA):
    pass

    def method_b(self):
        return self.val - 20

objB = SampleB(100)
