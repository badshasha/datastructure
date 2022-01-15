
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkList:
    def __init__(self):
        self.head = None

    def prepend(self, data): # add to front
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            temp = self.head
            while temp.next is not self.head.next:
                temp = temp.next
            temp.next = self.head

    def append(self, data):
        if not self.head:
           self.head = Node(data)
           self.head.next = self.head
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        if self.head is not None:
            temp = self.head
            while temp is not self.head:
                print(temp.value)
                temp = temp.next
        else:
            print("list empty")

