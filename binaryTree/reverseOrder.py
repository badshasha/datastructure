class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class Queue: # extract child nood from upper level node
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

class Stack: #  containing reverse order
    def __init__(self):
        self.items = []

    def push(self,value):
        self.items.append(value)

    def pop(self):
        if not self.__isEmpty():
            return self.items.pop()

    def __isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.__isEmpty():
            return self.items[-1].value

    def __len__(self):
        return len(self.items)


class BinaryTree:
    def __init__(self,value):
        self.root = Node(value)

    def printTree(self,type):
        if type == "reverseLevel":
            value = self.reverseLevelOrder(self.root)
            print(value)

    def reverseLevelOrder(self,start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        string = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            string += str(node.value) + '-'
        return string











b=BinaryTree(1)
b.root.left = Node(2)
b.root.right = Node(3)
b.root.left.left = Node(4)
b.printTree('reverseLevel')
