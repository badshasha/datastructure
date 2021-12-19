

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"


class SingleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __incrementCount(self):
        self.count += 1

    def __decrementCount(self):
        self.count -= 1

    def insertNode(self,value):
        n= Node(value)
        if self.head is None:
            self.head = n
            self.tail = n

        else:
            self.tail.next = n
            self.tail = n
        self.__incrementCount()

    def printAll(self):
        temp = 0
        node = self.head
        while(temp < self.count):
            print(node.value)
            node = node.next
            temp += 1


    def deleting(self,location):
        start = self.head
        last = None
        temp= 0
        while(temp < location-1):
            last = start
            start = start.next
            temp += 1
        last.next = start.next
        self.__decrementCount()






x = SingleLinkList()
x.insertNode(10)
x.insertNode(100)
x.insertNode(1000)

x.deleting(2)
x.printAll()
