# code written by shavnedra Ekanayake


# node class
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# single link list
    # |
    # |
    #  --------> create seperate node class


class SingleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def getElementCount(self):
        return self.count

    def __increase(self):
        self.count += 1

    def __decrease(self):
        self.count -= 1

    def __createNode(self, value):
        return Node(value)

    def AddElement(self, value):   # add element to the first position
        node = self.__createNode(value)
        if self.count == 0:
            self.head = node
            self.tail = node
            self.__increase()
        else:
            node.next = self.head
            self.head = node

    def RemoveElement(self):
        if self.count >= 0:
            node = self.head
            self.head = self.head.next
            self.__decrease()
            return node.value  # take the node value
        else:
            return None

    def headNodeValue(self):
        return self.head.value

    def Print(self):
        if self.count >= 0:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next
            print("list end")


# stack class connect to the SingleLink list
# stack stack operation done using single link list operation

class Stack:
    def __init__(self):
        self.link_list = SingleLinkList()

    def __validator(self, value):
        if value is None:
            print("stack is empty")
            return None
        return value

    def push(self, value):
        self.link_list.AddElement(value)
        print("value added success")

    def pop(self):
        value = self.link_list.RemoveElement()
        return self.__validator(value)

    def count(self):
        return self.link_list.getElementCount()

    def peek(self):
        value = self.link_list.headNodeValue()
        return self.__validator(value)


ss = Stack()
ss.push(5)
ss.push(6)
print(f'{ss.peek()} first peek')
ss.pop()
print(f'{ss.peek()} second peek')


# code success working




