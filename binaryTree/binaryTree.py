
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self,root):
        self.root = self.createNode(root)

    def createNode(self,value):
        return Node(value)

    def printTree(self,traversalType):
        if traversalType == 't':
            string = self.__preOrder(self.root,"")
            print(string)
        else:
            print("dont like you")

    def __preOrder(self,start,string):
        if start:
            string += (str(start.value) + '-')
            string = self.__preOrder(start.left, string)
            string = self.__preOrder(start.right, string)
        return string


#
b = BinaryTree('A')
b.root.left = Node('B')
b.root.right = Node('C')
b.root.left.left  = Node('E')

b.printTree('t')
