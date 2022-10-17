class Sample:
    dataa = 100
    _datab = 200
    __datac = 300
    __datad__ = 400

    def display(self):
        print(f"dataa = {self.dataa}")
        print(f"_datab = {self._datab}")
        print(f"__datac = {self.__datac}")
        print(f"__dataa__ = {self.__datad__}")

    def setDataa(self, val):
        self.dataa = val
    def set__Datac(self, val):
        self.__datac = val

    def getDataa(self):
        return self.dataa
    def get__Datac(self, val):
        return self.__datac

obja = Sample()

obja.display()
