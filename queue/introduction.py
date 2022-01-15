class Node:
    def __init__(self,value):
        self.value = value
        self.next_node = None

class SingleLinkList:
    def __init__(self,max_size = 10):
        self.max_size = max_size
        self.head = None
        self.tail = None
        self.count = 0

    def increase(self):
        self.count += 1

    def decrease(self):
        self.count -= 1

    def addNode(self,value):
        if self.max_size >= self.count:
            n = Node(value)
            if self.count == 0:
                self.head = n
                self.tail = n
            else:
                self.tail.next_node = n
                self.tail = n
            self.increase()

        else:
            print("queus is full")

    def removeNode(self):
        if self.count > 0:
            value = self.head
            self.head = self.head.next_node
            self.decrease()
            return value.value
        else:
            print("stack is empty")


class Queue:
    def __init__(self,max_length):
        self.link_list = SingleLinkList(max_length)

    # def __str__(self) -> str:
    #     values = [str(x) for x in self.list]
    #     return '\n'.join(values)

    def enqueue(self,value):
        # self.list.insert(0, value)
        self.link_list.addNode(value)

    def dequeue(self)->int:
        return self.link_list.removeNode()


q = Queue(10)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
value = q.dequeue()
print(q)
print(value)
