class Sample:
    def __init__(self, varx):
        self.__varx = varx

    def get_varx(self):
        return self.__varx

    def set_varx(self, varx):
        self.__varx = varx

obja = Sample(100)
objb = Sample(200)

print(obja.get_varx())

obja.set_varx(obja.get_varx() + objb.get_varx())

print(obja.get_varx())
