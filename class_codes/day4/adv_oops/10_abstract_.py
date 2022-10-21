from abc import abstractmethod, ABC

class SampleA(ABC):

    def method_a(self):
        pass

    @abstractmethod
    def method_b(self):
        print("love indian food")

class SampleB(SampleA):
    def method_b(self):
        super().method_b()
        print("and also cusines")

objy = SampleB()
objy.method_b()
