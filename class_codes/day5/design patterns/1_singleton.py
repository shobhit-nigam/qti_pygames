class Sample:
    __instance__ = None

    def __init__(self):

        if Sample.__instance__ is None:
            Sample.__instance__ = self
        else:
            raise Exception("can not create another instance")

    def get_instance():
        if not Sample.__instance____:
            Sample()
        return Sample.__instance__


obja = Sample()
print("---------")
objb = Sample()
