class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.size = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove_first(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.head is None:
            self.tail = None
        return removed_data
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

ll = SinglyLinkedList()

ll.add_first(20)
ll.add_first(10)
ll.add_last(30)
ll.add_last(40)

ll.display()

ll.remove_first()
ll.display()
