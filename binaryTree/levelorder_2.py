class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,value):
        self.items.insert(0,value)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return str(self.items[-1].value)

    def __len__(self):
        return len(self.items)


class BinaryTree:
    def __init__(self,value):
        self.root = self.__createNode(value)

    def __createNode(self,value):
        return Node(value)

    def printTree(self):
        string = self.__levelOrder(self.root)
        print(string)

    def __levelOrder(self,start):
        string = ""
        queue = Queue()
        queue.enqueue(start)
        while len(queue) > 0:
            string += queue.peek() + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return string


b=BinaryTree(1)
b.root.left = Node(2)
b.root.right = Node(3)
b.root.left.left = Node(4)
b.printTree()
