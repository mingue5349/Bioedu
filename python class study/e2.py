class Stock:
    def __init__(self, list):
        self.list = list

    def sum(self):
        j = 0
        for i in self.list:
            j += i
        return j

    def avg(self):
        j = 0
        for i in self.list:
            j += i
        j = j/len(self.list)
        return j

cal1 = Stock([1,2,3,4,5])

print(cal1.sum())
print(cal1.avg())