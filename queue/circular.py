
class CircleLinkList:
    def __init__(self, maxLength):
        self.maxLength = maxLength
        self.list = [None for x in range(maxLength)]
        self.start = -1
        self.top = -1

    def __str__(self):
        value = [str(x) for x in self.list]
        return ''.join(value)

    def __isFull(self):
        if (self.top + 1) % self.maxLength == self.start:
            return True
        return False

    def __isEmpty(self):
        if self.top == -1:
            return True

    def Add(self,value):
        if self.__isEmpty():
            self.start += 1
            self.top += 1
            self.list[self.top] = value
        elif not self.__isFull():
            self.top = (self.top + 1) % self.maxLength
            self.list[self.top] = value
        else:
            print("full")

    def Remove(self):
        if not self.__isEmpty():
            value = self.list[self.start]
            self.list[self.start] = None
            self.start = (self.start + 1) % self.maxLength
            return value


c = CircleLinkList(5)
c.Add(1)
c.Add(2)
c.Add(3)
c.Add(4)
c.Add(5)

print(c)

c.Remove()
print(c)

c.Add(6)

print(c)

c.Remove()
c.Remove()
print(c)

