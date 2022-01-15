
class Node:
    def __inti__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,value):
        self.root = self.__createNode(value)

    def __createNode(self,value)->Node:
        return Node(value)

    def __insert(self,node,value):
        if node.value > value:
            if node.left is None:
                node.left = self.__createNode(value)
            else:
                self.__insert(node.left,value)
        elif node.value < value:
            if node.right is None:
                node.right = self.__createNode(value)
            else:
                self.__insert(node.right,value)
        else: # same value
            print("value already stored in tree structure")

    def inserting(self,value):
        if self.root is None:
            self.root = self.__createNode(value)
        else:
            self.__insert(self.root,value)

    def __find(self,node,value):
        if value > node.value and node.right:
            return self.__find(node.right,value)
        elif value < node.value and node.left:
            return self.__find(node.left,value)
        if value == node.value:
            return True


    def search(search):
        if self.root:
            found = self.__find(data,self.root)
            if found:
                return True
            return False
        else:
            return None
