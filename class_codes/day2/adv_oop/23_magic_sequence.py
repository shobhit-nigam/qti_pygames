class CustomList:

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # if key invalid, raise error
        return self.values[key]

    def __setitem__(self, key, value):
        # if key invalid, raise error
        self.values[key]   = value

    def __delitem__(self, key, value):
        # if key invalid, raise error
        self.values[key]   = value

    def __iter__(self):
        return iter(self.values)

    def last(self):
        # get last element
        return self.values[-1]






objc = CustomList([100, 200, 300, 400, 500])
objd = CustomList()

print(objc[2])
objc[3] = "hello"
print(objc[3])
