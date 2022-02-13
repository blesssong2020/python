#  globals().clear()

s = "123456"
def leetcode_20(s):
    my_stack = []
    map = {")" : "(", "]" : "[", "}": "{"}
    for x in s:

        print(my_stack)
        if x == "(" or x == "[" or x == "{":
            my_stack.append(x)
        elif len(my_stack) > 0 and my_stack[-1] == map[x]:
            my_stack.pop()
        else:
            return False

        """elif len(my_stack) > 0 and x == ")" and my_stack[-1] == "(":
            my_stack.pop()
        elif len(my_stack) > 0 and x == "]" and my_stack[-1] == "[":
            my_stack.pop()
        elif len(my_stack) > 0 and x == "}" and my_stack[-1] == "{":
            my_stack.pop()
        else:
            return False"""

    return my_stack == []

from my_stack_class import Stack

def my_leetcode_20_2(s):
    my_stack = Stack()
    map = {")" : "(", "]" : "[", "}": "{"}
    for x in s:
        if x in ["(", "[", "{"]:
            my_stack.push(x)
        elif my_stack.peek() == map[x]:
            my_stack.pop()
        else:
            return False
    return my_stack.isEmpty()




def reverse_str(s):
    my_stack = Stack()
    for x in s:
        my_stack.push(x)

    new_str = ""
    while not my_stack.isEmpty():
        new_str += my_stack.peek()
        my_stack.pop()
    return new_str

x = 10000
def dec_to_bin(x, k):
    my_stack = Stack()
    if x == 0:
        return 0

    while x:
        my_stack.push(x % k)
        x = int(x/k)

    my_result = []
    #map = {0:"0", 1:"0", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7"}
    l = [0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f"]
    print(map)
    while not my_stack.isEmpty():
        my_result.append(str(l[my_stack.peek()]))
        my_stack.pop()

    return my_result

print(dec_to_bin(x, 16))


class MaxStack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        self.data.pop(-1)

    def top(self):
        if self.data:
            return self.data[-1]

    def peekMax(self):
        if self.data:
            return max(self.data)
        else:
            print("stack is empty")

    def popMax(self):
        if self.data:
            return max(self.data).pop(-1)
        else:
            print("stack is empty")

def leetcode_876_middleNode(self, head):

    curr_node = head
    count = 0
    while curr_node:
        count += 1
        curr_node = curr_node.next


    curr_node = head
    for i in range(int(round(count/2))):
        curr_node = curr_node.next

    return curr_node

def leetcode_142_detectCycle(self, head):

    my_list = []
    curr_node = head
    count = 0
    if not curr_node or not curr_node.next:
        return None

    while curr_node.next and curr_node.next not in my_list:
        my_list.append(curr_node)
        count += 1
        curr_node = curr_node.next

    return curr_node.next
