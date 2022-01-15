

class Node:
    def __init__(self,data):
        self.value = data
        self.next = None
        self.prev = None

class DoubleLinkList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        list = []
        while temp is not None:
            list.append(str(temp.value))
            temp = temp.next
        return ','.join(list)

    def __isEmpty(self):
        return self.head is None

    def __createNode(self,data):
        return Node(data)

    def __findLast(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp

    def append(self,data):
        n = self.__createNode(data)
        if self.__isEmpty():
            self.head = n
        else:
            temp = self.__findLast()
            temp.next = n
            n.prev = temp


    def prepend(self,data):
        n = self.__createNode(data)
        if self.__isEmpty():
            self.head = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n

    def pop(self):
        if self.__isEmpty():
            return 0
        else:
            temp = self.__findLast()
            prev = temp.prev
            prev.next = None
            return temp.value






d = DoubleLinkList()
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.append(8)
d.prepend(10)
d.prepend(11)
print(d)
print(f' last value {d.pop()}')
print(d)
print(f' last value {d.pop()}')
print(d)
