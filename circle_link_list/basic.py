

class Node:
    def __init__(self,value):
        self.value = value
        self.next = none


class CircleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.conut = 0

    def __countIncrement(self):
        self.conut += 1

    def __createNode(self,value):
        return Node(value)

    def __positionFinder(self,position):
        if position < self.conut:
            temp = 0
            start = self.head
            while temp < position:
                start = start.next
                temp+=1
            return start  # location of the node
        else:
            raise Exception("invalid position ")


    def addNode(self,value):
        node = self.__createNode(value)
        if self.head is not None:
            self.head = node
            self.tail = node
            self.tail.next = node
        else:
            temp_node = self.tail
            node.next = head
            temp_node.next = node
            self.tail = node
        self.__countIncrement()

    def inserting(self,position,value):
        new_node = self.__createNode(value)
        old_node = self.__positionFinder(position)
        new_node.next = old_node.next
        old_node.next = new_node

    def printAll(self):
        if self.head is not None:
            start_node = self.head;
            while start_node != self.head:
                print(start_node.value)
                start_node = start_node.next
        else:
            raise Exception("[-] CircleLink List not created yet : sudgessions : use \"CriclelinkList.addNode\" to create new list ")
