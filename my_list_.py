# singly linked list vs doubled linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next

        curr_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        curr_node = self.head
        print_list = []
        while curr_node != None:
            print_list.append(curr_node.data)
            curr_node = curr_node.next
        print(print_list)

    def listLength(self):
        count = 0
        curr_node = self.head
        while curr_node != None:
            count += 1
            curr_node = curr_node.next
        return count

    def list_len_rec(self, node):
        if not node:
            return 0
        else:
            return 1 + self.list_len_rec(node.next)

    def insert(self, prev_node, data):
        if prev_node:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def get_node(self, pos):
        node_number = self.listLength()
        if pos >= node_number:
            return None

        curr_node = self.head
        count = 0
        while curr_node:
            if count == pos:
                return curr_node
            else:
                curr_node = curr_node.next
                count += 1

    def deletion(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            return

        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node:
            prev_node.next = curr_node.next
            curr_node = None

    def delete_pos(self, pos):
        length = self.listLength()
        if pos >= length:
            return

        if pos == 0:
            curr_node = self.head
            self.head = self.head.next
            curr_node = None
            return

        curr_node = self.get_node(pos)
        prev_node = self.get_node(pos - 1)
        prev_node.next = curr_node.next
        curr_node = None







def test_myList():
    list_1 = LinkedList()
    list_1.append(3)
    list_1.append(2)
    list_1.append(1)
    list_1.prepend(0)
    list_1.printList()
    node_2 = list_1.get_node(3)
    print(node_2.data)
    list_1.insert(node_2, 10)
    list_1.printList()
    list_1.deletion(20)
    list_1.printList()
    list_1.delete_pos(2)
    list_1.printList()
    print(list_1.list_len_rec(list_1.get_node(100)))


test_myList()


