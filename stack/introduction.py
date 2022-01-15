

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SingleLinkList:
    def __init__(self):
        self.first = None
        self.tail = None
        self.count  = 0

    def addElement(self,value):
        node  = Node(value)
        if self.count == 0:
            self.first = node
            self.tail = node
        else:
            node.next = self.first
            self.first = node
        self.count += 1

    def removeNode(self):
        if self.count > 1:
            last = self.first
            self.first =  self.first.next
            self.count -= 1
            return last
        elif self.count == 1:
            last = self.first
            self.first = None
            self.tail = None
            self.count -= 1
            return last
        else:
            print("no element on the link list ")



class Stack:
    def __init__(self):
        self.count = 0
        self.array = []
        self.singleLinkList = SingleLinkList()

    def __increase(self):
        self.count += 1

    def __decrease(self):
        self.count -= 1

    def __iftestCount(self):
        return self.count > 0

    def AddElement(self,value):
        # self.array.append(value)
        self.singleLinkList.addElement(value)
        self.__increase()

    def pop(self):
        if self.__iftestCount():
            value=self.array[self.count - 1]
            v2 = self.singleLinkList.removeNode()
            self.__decrease()
            return value
        else:
            print("no element")

    def peek(self):
        if (self.__iftestCount()):
            print(self.array[self.count-1])
        else:
            print("no element")


s = Stack()
s.AddElement(2)
s.peek()
s.AddElement(3)
s.peek()
value = s.pop()
print(value)
s.peek()
value = s.pop()
value = s.pop()
