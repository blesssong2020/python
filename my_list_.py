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
        while curr_node:
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

    def get_last_node(self):
        if not self.head:
            return None
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        return curr_node

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

    def remove_duplicate(self):
        my_dict = {}
        prev_node = None
        curr_node = self.head
        while curr_node:
            if curr_node.data not in my_dict:
                my_dict[curr_node.data] = 1
                prev_node = curr_node
                #curr_node = prev_node.next
            else:
                prev_node.next = curr_node.next
                curr_node = None
                #curr_node = prev_node.next
            curr_node = prev_node.next

    def swap(self, k1, k2):
        if k1 == k2:
            return

        k1_prev_node = None
        k1_curr_node = self.head
        while k1_curr_node and k1_curr_node.data != k1:
            k1_prev_node = k1_curr_node
            k1_curr_node = k1_curr_node.next

        k2_prev_node = None
        k2_curr_node = self.head
        while k2_curr_node and k2_curr_node.data != k2:
            k2_prev_node = k2_curr_node
            k2_curr_node = k2_curr_node.next

        if not k1_curr_node or not k2_curr_node:
            return

        if k1_prev_node:
            k1_prev_node.next = k2_curr_node
        else:
            self.head = k2_curr_node

        if k2_prev_node:
            k2_prev_node.next = k1_curr_node
        else:
            self.head = k1_curr_node

        k1_curr_node.next, k2_curr_node.next = k2_curr_node.next, k1_curr_node.next

    def reverse(self):
        prev_node = None
        curr_node = self.head
        next_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node

    def reverse_recursive(self):
        def helper(prev, curr):
            if not curr:
                return prev

            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

            return helper(prev, curr)

        self.head = helper(None, self.head)

    def merge(self, list):
        curr1 = self.head
        curr2 = list.head
        node = None
        new_head = None
        if not curr1:
            return curr2
        if not curr2:
            return curr1

        if curr1.data <= curr2.data:
            new_head = curr1
            curr1 = curr1.next
        else:
            new_head = curr2
            curr2 = curr2.next

        node = new_head
        while curr1 and curr2:
            if curr1.data <= curr2.data:
                node.next = curr1
                curr1 = curr1.next
            else:
                node.next = curr2
                curr2 = curr2.next
            node = node.next

        if not curr2:
            node.next = curr1
        else:
            node.next = curr2
        self.head = new_head
        return self.head

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
            return

        curr_node = self.head
        while curr_node.next != self.head:
            curr_node = curr_node.next
        curr_node.next = new_node
        new_node.next = self.head

    def printList(self):
        my_list = []
        curr_node = self.head
        while curr_node:
            my_list.append(curr_node.data)
            curr_node = curr_node.next
            if curr_node == self.head:
                break
        print(my_list)

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        curr_node = self.head
        while curr_node.next != self.head:
            curr_node = curr_node.next
        curr_node.next = new_node
        new_node.next = self.head

        self.head = new_node

    def get_last_node(self):
        if not self.head:
            return None
        curr_node = self.head
        while curr_node.next != self.head:
            curr_node = curr_node.next
        return curr_node

    def delete(self, key):
        if not self.head:
            return
        prev_node = None

        if self.head.data == key:
            last_node = self.get_last_node()
            if last_node == self.head:
                self.head = None
                return

            last_node.next = self.head.next
            self.head = None
            self.head = last_node.next
            return

        prev_node = self.head
        curr_node = self.head.next
        while curr_node != self.head:
            if curr_node.data == key:
                prev_node.next = curr_node.next
                curr_node = None
                return
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node.data == key:
            prev_node.next = curr_node.next
            curr_node = None

def isa_circular_list(list):
    curr_node = list.head
    while curr_node:
        if curr_node.next == list.head:
            return True
        curr_node = curr_node.next
    return False












def test_myList():
    list_1 = LinkedList()
    list_2 = LinkedList()
    list_1.append(1)
    list_1.append(3)
    list_1.append(4)
    list_1.append(5)
    list_1.append(10)
    list_1.printList()
    list_2.append(2)
    list_2.append(7)
    list_2.append(9)
    list_2.append(20)
    list_2.printList()
    list_1.get_last_node().next

def test_2():
    cl_2 = CircularLinkedList()
    cl_2.append(2)
    cl_2.append(10)
    cl_2.append(100)
    cl_2.prepend(222)
    cl_2.prepend(444)
    cl_2.printList()
    #cl_2.get_last_node().next.next.data
    #print("AAA")
    cl_2.delete(222)
    cl_2.printList()
    pass



test_2()



