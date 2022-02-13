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

    def delete(self, key):
        curr_node = self.head
        if self.head.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        while curr_node:
            if curr_node.data == key:
                if not curr_node.next:
                    prev_node = curr_node.prev
                    prev_node.next = None
                    curr_node = None
                    return
                prev_node = curr_node.prev
                next_node = curr_node.next
                next_node.prev = prev_node
                prev_node.next = next_node
                curr_node = None
                return
            curr_node = curr_node.next

    def get_node(self, data):
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                return curr_node
            curr_node = curr_node.next
        return None

    def delete_node(self, node):
        curr_node = self.head
        if self.head == node:
            self.head = curr_node.next
            curr_node = None
            return

        while curr_node:
            if curr_node == node:
                if not curr_node.next:
                    prev_node = curr_node.prev
                    prev_node.next = None
                    curr_node = None
                    return
                prev_node = curr_node.prev
                next_node = curr_node.next
                next_node.prev = prev_node
                prev_node.next = next_node
                curr_node = None
                return
            curr_node = curr_node.next

    def reverse(self):
        if not self.head or not self.head.next:
            return

        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            prev_node = curr_node.prev

            curr_node.prev = next_node
            curr_node.next = prev_node

            self.head = curr_node
            curr_node = next_node

    def remove_duplicate(self):
        my_dict = {}
        curr_node = self.head

        while curr_node:
            if curr_node.data not in my_dict:
                my_dict.update({curr_node.data:0})
            else:
                self.delete_node(curr_node)
            curr_node = curr_node.next

# list [5,8,7,1,10] sum combination no duplicate


def test():
    d_1 = DLL()
    d_1.append(1)
    d_1.append(7)
    d_1.append(10)
    d_1.prepend(8)
    d_1.prepend(5)
    d_2 = DLL()
    d_2.append(7)
    d_2.append(10)
    d_1.append(10)
    d_1.append(7)
    #node1 = d_1.get_node(10)
    #print(node1)
    #node2 = d_2.get_node(10)
    #print(node2)
    #print(node1 == node2)
    #d_1.delete_node(d_2.get_node(10))
    d_1.remove_duplicate()
    print("candi")
    d_1.printList()

#if __name__ == '__main__':
    #test()


test_dll = DLL()
test_dll.append(5)
test_dll.append(8)
test_dll.append(7)
test_dll.append(1)
test_dll.append(10)
result = []
def combination_sum_linkedlist(target, combination, curr_node = test_dll.head):
    if target == 0:
        result.append(list(combination))
        return

    if target < 0:
        return

    while curr_node:
        combination.append(curr_node.data)
        print(combination)
        combination_sum_linkedlist(target - curr_node.data, combination, curr_node)
        combination.pop()
        curr_node = curr_node.next

def test_result():
    combination_sum_linkedlist(10, [])
    print(result)
    print(len(result), "length")

test_result()


