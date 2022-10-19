class CustomList:

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        if key<0:
            raise IndexError("negative indices not allowed")
        return self.values[key]

    def __setitem__(self, key, value):
        # if key invalid, raise error
        self.values[key]   = value

    def __delitem__(self, key, value):
        # if key invalid, raise error
        self.values[key]   = value

    def __iter__(self):
        return iter(self.values)



    def half(self):
        half_length = len(self.values)//2
        return self.values[0:half_length]

objc = CustomList([100, 200, 300, 400, 500, 600])
objd = CustomList()

print(objc[-2])
