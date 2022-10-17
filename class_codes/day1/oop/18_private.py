class Sample:
    dataa = 100
    _datab = 200
    __datac = 300
    __datad__ = 400

    def dispaly(self):
        print(f"dataa = {self.dataa}")
        print(f"_datab = {self._datab}")
        print(f"__datac = {self.__datac}")
        print(f"__dataa__ = {self.__datad__}")

obja = Sample()

print(f"dataa = {obja.dataa}")
print(f"_datab = {obja._datab}")
# error
print(f"__datac = {obja.__datac}")
print(f"__datad__ = {obja.__datad__}")
