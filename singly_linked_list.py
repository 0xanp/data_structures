
class Node:
    def __init__(self,data,nxt):
        self.data = data
        self.nxt = nxt

class Singly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = self.head
    # Insertion:  O(1)
    # Desc: adding a node with the given value at after the tail
    # Cases: 1. Empty List -> Adding the node as head and tail
    #        2. Add the node at the end of the list and update the tail
    #        reference accordingly
    # Params: value
    # Return: nothing
    def insert(self,value):
        temp = Node(value,None)
        if not self.head:
            self.head = temp
            self.tail = self.head
        else:
            self.tail.nxt = temp
            self.tail = temp
    # Searching: O(1)
    # Desc: Traversing and checking if the list contain the target value
    # 