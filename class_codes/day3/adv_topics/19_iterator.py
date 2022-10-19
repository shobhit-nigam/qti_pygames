class Series:

    def __init__(self, num=0):
        self.num = num

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.num:
            res = 2 ** self.n
            self.n = self.n + 1
            return res
        else:
            raise StopIteration

listx = Series(3)

obji = iter(listx)

for val in Series(4):
    print(val)
