

class Node:
    def __init__(self,value):
        self.value = value
        self.nextNode = None

class CircleLinkList:
    def __init__(self,maxLength):
        self.maxLength = maxLength
        self.count += 0
        self.head = None
        self.tail = None

    def __createNode(self,value)->Node:
        return Node(value)

    def __ifFull(self):
        if self.count == self.maxLength:
            return True
        return False

    def addElement(self,value):
        n = self.__createNode()
        if self.head is None:
            self.head = n
            self.tail = n
            self.count += 1
        else:
            if not self.__ifFull():
                self.tail.nextNode = n
                self.tail = n
                # increase the count
                self.count += 1
            else:
                print("list is full")
