

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Stack:
    def __init__(self):
        self.items = []

    def push(self,value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def peek(self):
        return self.items[-1].value


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,value):
        self.items.insert(0,value)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1].value

    def __len__(self):
        return len(self.items)


class BinaryTree:
    def __init__(self):
        self.root = None

    def __createNode(self,value):
        return Node(value)

    def __insertRec(self,node,value):
        if node.value > value:
            if node.left is None:
                node.left = self.__createNode(value)
            else:
                self.__insertRec(node.left,value)
        elif node.value < value:
            if node.right is None:
                node.right = self.__createNode(value)
            else:
                self.__insertRec(node.right,value)
        else:
            print("value already stored (ducplicated value node allowed)")

    def insert(self,value):
        if self.root is None:
            self.root = self.__createNode(value)
        else:
            self.__insertRec(self.root,value)

    def __searching(self,node,value):
        if node is None:
            return False
        elif node.value > value and node.left:
            return self.__searching(node.left, value)
        elif node.value < value and node.right:
            return self.__searching(node.right, value)
        elif node.value == value:
            return True
        else:
            return False

    def printLevel(self,node,string):
        if node is  not None:
            string += str(node.value) + '-'
            string = self.printLevel(node.left, string)
            string = self.printLevel(node.right, string)
        return string

    def printLeft(self,node,string):
        if node is not None:
            string = self.printLevel(node.left, string)
            string += str(node.value) + '-'
            string = self.printLevel(node.right, string)
        return string

    def printRight(self,node,string):
        if node is not None:
            string = self.printLevel(node.right, string)
            string += str(node.value) + '-'
            string = self.printLevel(node.left, string)
        return string

    def printOrderLevel(self, start):
        string = ""
        queue = Queue()
        if  start is not None:
            queue.enqueue(start)
            while len(queue) > 0:
                string += str(queue.peek()) + "-"
                node = queue.dequeue()
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            return string
        else:
            return "tree empty"

    def printReverseLevelOrder(self,start):
        if start is not None:
            string = ""
            queue = Queue()
            stack = Stack()
            queue.enqueue(start)
            while len(queue) > 0:
                node = queue.dequeue()
                stack.push(node)
                if node.right:
                    queue.enqueue(node.right)
                if node.left:
                    queue.enqueue(node.left)

            while len(stack) > 0:
                node = stack.pop()
                string += str(node.value) + "-"
            return string
        else:
            return "empty"

    def print(self,type):
        if type == "l":
            string = self.printLevel(self.root,"")
        elif type == 'p':
            string = self.printLeft(self.root,"")
        elif type == 'z':
            string = self.printRight(self.root,"")
        elif type == 'level':
            string = self.printOrderLevel(self.root)
        elif type == "reverse":
            string = self.printReverseLevelOrder(self.root)
        print(string)


    def search(self,value):
        if self.root is None:
            return False
        else:
            return self.__searching(self.root,value)


b = BinaryTree()

b.insert(10)
b.insert(9)
b.insert(11)
b.insert(13)
b.print('l')
b.print('p')
b.print('z')
b.print('level')
b.print('reverse')
# print(b.search(13))


