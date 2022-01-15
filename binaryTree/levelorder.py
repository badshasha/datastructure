class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.item = []

    def __isEmpty(self):
        return len(self.item) == 0

    def enqueue(self,value):
        self.item.insert(0,value)

    def dequeue(self):
        if not self.__isEmpty():
            return self.item.pop()

    def peek(self):
        if not self.__isEmpty():
            return self.item[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.item)



class BinaryTree:
    def __init__(self,value):
        self.root = Node(value)
        self.array = []

    def printBinaryTree(self,type):
        if type == "level":
            string = self.__levelOrder(self.root)
            print(string)

    def __levelOrder(self,start):
        if start is None:
            return
        queues = Queue()
        queues.enqueue(start)
        string = ""
        while len(queues) > 0:
            string += str(queues.peek()) + '-'
            node = queues.dequeue()
            if node.left:
                queues.enqueue(node.left)
            if node.right:
                queues.enqueue(node.right)
        return string



b=BinaryTree(1)
b.root.left = Node(2)
b.root.left.left = Node(5)
b.root.right = Node(3)
b.printBinaryTree('level')
