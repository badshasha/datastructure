# train look like linked list
# creating link list

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class SingleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __countIncrement(self):
        self.count += 1

    def addNode(self,value=None):  # using only head
        n = Node(value)
        if self.head is None:
            self.head = n
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = n
        self.__countIncrement()

    def addNodeUsingTail(self,value=None):
        n = Node(value)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.__countIncrement()


# i didnt check this part please check it later 
    def addNodeLocation(self,location=None,value=None):
        n = Node(value)
        if self.head is None:
            self.head = n
            self.tail = n
        else if location == None :
            self.tail.next = n
            self.tail = n
        else:
            if self.count >= location:
                counter = 0
                temp = self.head
                prev_next = None
                while(counter < location -1):
                    temp = temp.next
                prev_next = temp.next
                n.next = prev_next
                temp.next = n
            else:
                print("location not valied ")





s = SingleLinkList()
s.addNode(5)
s.addNode(7)
print(s.head.value , s.head.next.value , s.head.next.next)


x =SingleLinkList()
x.addNodeUsingTail(10)
x.addNodeUsingTail(20)
print(x.head.value , x.tail.value)
