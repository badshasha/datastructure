class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self,value):
        self.root = self.__createNewNode(value)

    def print(self,type):
        start = self.root
        string = ""
        if type == 'pre':
            string = self.__preOrder(start, string)
        elif type == 'in':
            string = self.__inOdererTraversal(start,string)
        elif type == 'post':
            string = self.__postOrder(start,string)
        print(string)

    def __inOdererTraversal(self, start, string):
        # left -> root -> right
        if start:
            string = self.__inOdererTraversal(start.left, string)
            string += str(start.value)
            string = self.__inOdererTraversal(start.right, string)
        return string

    def __preOrder(self, start, string):
        # root -> left -> right
        if start:
            string += str(start.value) + " "
            string = self.__preOrder(start.left, string)
            string = self.__preOrder(start.right, string)
        return string

    def __postOrder(self, start, string):
        # left -> root -> right
        if start:
            string = self.__postOrder(start.right, string)
            string = self.__postOrder(start.left, string)
            string += str(start.value)
        return string

    def __createNewNode(self, value):
        return Node(value)

    def __inserting(self,value):
        self.__createNewNode(value)


b = BinaryTree(4)
b.root.left = Node(5)
b.root.right = Node(6)
b.print('post')




