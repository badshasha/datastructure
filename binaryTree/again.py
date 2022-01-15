# code by badshasha
# testing binary tree functionalities

# class contain node information
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# class queus
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,node):
        self.items.insert(0,node)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1].value

    def __len__(self):
        return len(self.items)


# binary tree data structure
class BinaryTree:
    def __init__(self):
        self.root = None

    def __create(self, value):
        return Node(value)

    def __inserting(self, node, value):
        if node is None:
            node = self.__create(value)
        elif node.value > value:
            if node.left is None:
                node.left = self.__create(value)
                print(f"value enterd success [left] {value}")
            else:
                self.__inserting(node.left, value)
        elif node.value < value:
            if node.right is None:
                node.right = self.__create(value)
                print(f"value enterd success [right] {value}")
            else:
                self.__inserting(node.right, value)
        elif node.value == value:
            print("value already exist on the tree")

    def __searching(self, node, value):
        if node.value == value:
            return True
        elif node.value > value and node.left:
            return self.__searching(node.left, value)
        elif node.value < value and node.right:
            return self.__searching(node.right, value)
        else:
            return False

    def search(self, value):
        if self.root is None:
            return False
        else:
            return self.__searching(self.root, value)

    def insert(self, value):
        if self.root is None:
            self.root = self.__create(value)
            print(f"root add {value}")
        else:
            self.__inserting(self.root, value)

    def __printt(self, node, string) -> str:
        if node is not None:
            string += str(node.value) + "-"
            string = self.__printt(node.left,string)
            string = self.__printt(node.right,string)
        return string

    def __printl(self,node,string) -> str:
        if node is not None:
            string = self.__printt(node.left,string)
            string += str(node.value) + "-"
            string = self.__printt(node.right,string)
        return string

    def orderPrint(self,node):
        if node is not None:
            string = ""
            queue  = Queue()
            queue.enqueue(node)
            while len(queue) > 0:
                string += str(queue.peek()) + "-"
                node = queue.dequeue()
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            return string
        return "empty tree"



    def print(self, type):
        if type == 't':
            string = self.__printt(self.root, "")
        if type == 'l':
            string = self.__printl(self.root,"")
        if type == 'order':
            string = self.orderPrint(self.root)
        print(string)


b = BinaryTree()
b.insert(1)
b.insert(2)
b.insert(4)
b.insert(3)
print(b.search(51))
b.print('t')
b.print('l')
b.print('order')