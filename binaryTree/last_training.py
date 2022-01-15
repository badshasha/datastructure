# code by 'badshasha'

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def __createNewNode(self, value) -> Node:
        return Node(value)

    def __addElement(self, node, value):
        if node.value > value:
            if node.left is None:
                node.left = self.__createNewNode(value)
            else:
                self.__addElement(node.left, value)
        elif node.value < value:
            if node.right is None:
                node.right = self.__createNewNode(value)
            else:
                self.__addElement(node.right, value)
        else:
            print("value already exist")

    def AddElement(self, value) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self.__addElement(self.root, value)

    def printInfo(self,node,string):
        if node is not None:
            string += str(node.value)
            string  = self.printInfo(node.left , string)
            string =  self.printInfo(node.right,string)
        return string

    def printTree(self, type):
        if type == 't':
            return self.printInfo(self.root,"")



b = BinaryTree()
b.AddElement(3)
b.AddElement(2)
b.AddElement(2)
b.AddElement(5)
print(b.printTree('t'))
