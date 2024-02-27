class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL(Node):
    def __init__(self, start=None):
        self.start = start
    
    def is_empty(self):
        if self.start == None:
            return True
        return False