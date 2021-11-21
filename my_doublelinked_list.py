# doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = new_node
        new_node.prev = curr_node

    def printList(self):
        my_list = []
        curr_node = self.head
        while curr_node:
            my_list.append(curr_node.data)
            curr_node = curr_node.next
        print(my_list)

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_after(self, key, data):
        new_node = Node(data)
        curr_node = self.head
        while curr_node:
            if curr_node.data == key:
                next_node = curr_node.next
                curr_node.next = new_node
                new_node.prev = curr_node
                if next_node:
                    new_node.next = next_node
                    next_node.prev = new_node
                return
            curr_node = curr_node.next

    def insert_before(self, key, data):
        new_node = Node(data)
        curr_node = self.head

        while curr_node:
            if curr_node.data == key:
                if not curr_node.prev:
                    self.prepend(data)
                    return
                prev_node = curr_node.prev
                curr_node.prev = new_node
                new_node.prev = prev_node
                prev_node.next = new_node
                new_node.next = curr_node
                return
            else:
                curr_node = curr_node.next








def test():
    d_1 = DLL()
    d_1.append(1)
    d_1.append(7)
    d_1.append(10)
    d_1.prepend(8)
    d_1.prepend(5)
    d_1.printList()
    d_1.insert_before(5,19)
    d_1.insert_before(10,18)
    d_1.printList()

if __name__ == '__main__':
    test()
