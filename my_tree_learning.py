#binary tree, node, child nodes, left/right child vs leaf(non child)
# preoder: root -> left -> right
# inorder: left -> root -> right
# postorder: left -> right -> root

from my_stack_class import Stack
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self, root):
        self.root = root

    def pre_order_print(self, start_node, result=""):
        if not start_node:
            return result
        #print("node value ", start_node.data)
        result += str(start_node.data) + "->"
        result = self.pre_order_print(start_node.left, result)
        result = self.pre_order_print(start_node.right, result)

        return result

    def in_order_stack_print(self):
        result = []
        if not self.root:
            return result
        my_stack = Stack()
        curr_node = self.root
        while True:
            if curr_node:
                my_stack.push(curr_node)
                curr_node = curr_node.left
            else:
                if not my_stack.isEmpty():
                    node = my_stack.top()
                    my_stack.pop()
                    result.append(node.data)
                    curr_node = node.right
                else:
                    break
        return result

    def in_order_print(self, start_node, result = ""):
        if not start_node:
            return result
        result = self.in_order_print(start_node.left, result)
        result += str(start_node.data)+"->"
        result = self.in_order_print(start_node.right, result)

        return result

    def pre_order_stack_print(self):
        result = []
        if not self.root:
            return result
        my_stack = Stack()
        my_stack.push(self.root)
        while not my_stack.isEmpty():
            curr_node = my_stack.top()
            my_stack.pop()
            result.append(curr_node.data)
            if curr_node.right:
                my_stack.push(curr_node.right)
            if curr_node.left:
                my_stack.push(curr_node.left)
        return result

    def post_order_print(self, start_node, result = ""):
        if not start_node:
            return result

        result = self.post_order_print(start_node.left, result)
        result = self.post_order_print(start_node.right, result)
        result += str(start_node.data) + "->"

        return result

    def post_order_stack_print(self, result = []):
        my_stack = Stack()
        my_stack.push(self.root)
        if not self.root:
            return result
        while not my_stack.isEmpty():
            curr_node = my_stack.top()
            my_stack.pop()
            result.append(curr_node.data)
            if curr_node.left:
                my_stack.push(curr_node.left)
            if curr_node.right:
                my_stack.push(curr_node.right)
        result.reverse()
        return result


    def post_order_stack_print_3(self, result = []):
        my_stack = Stack()
        if not self.root:
            return result
        curr_node = self.root
        while True:
            while curr_node:
                if curr_node.right:
                    my_stack.push(curr_node.right)
                my_stack.push(curr_node)
                curr_node = curr_node.left
            curr_node = my_stack.top()
            my_stack.pop()

            if curr_node.right == my_stack.top():
                my_stack.pop()
                my_stack.push(curr_node)
                curr_node = curr_node.right
            else:
                result.append(curr_node.data)
                curr_node = None

            if my_stack.isEmpty():
                break
        return result


    def level_print(self, result=[]):
        my_queue = []
        if not self.root:
            return result
        curr_node = self.root
        my_queue.append(curr_node)
        while my_queue:
            node = my_queue.pop()
            result.append(node.data)
            if node.left:
                my_queue.insert(0,node.left)
            if node.right:
                my_queue.insert(0,node.right)
        return result



    def post_order_stack_print_2(self):
        result = []
        if not self.root:
            return result
        my_stack = Stack()
        curr_node = self.root
        repeat_node = None
        while True:
            while curr_node:
                my_stack.push(curr_node)
                curr_node = curr_node.left

            pre_node = my_stack.top()
            if pre_node.right and repeat_node != pre_node.right:
                curr_node = pre_node.right
            else:
                my_stack.pop()
                result.append(pre_node.data)
                repeat_node = pre_node

            if my_stack.isEmpty():
                break

        return result

    def level_reverse_print(self):
        if not self.root:
            return []
        result = []
        my_queue = [self.root]
        while my_queue:
            curr_node = my_queue.pop(0)
            result.append(curr_node.data)
            if curr_node.right:
                my_queue.append(curr_node.right)
            if curr_node.left:
                my_queue.append(curr_node.left)
        result.reverse()
        return result

    """
    class Solution(object):
    def levelOrderBottom(self, root):
        result = []
        if not root:
            return result
        my_queue = [root]
        
        while my_queue:
            count = len(my_queue)
            temp = []
            while count>0:
                curr_node = my_queue.pop(0)
                temp.append(curr_node.val)
                count -= 1
                if curr_node.left:
                    my_queue.append(curr_node.left)
                if curr_node.right:
                    my_queue.append(curr_node.right)
            result.append(temp)   
        result.reverse()
        return result
    """



    def count(self):
        if not self.root:
            return 0
        curr_node = self.root
        def helper(curr_node):
            if not curr_node:
                return 0
            return 1 + helper(curr_node.left) + helper(curr_node.right)
        return helper(curr_node)

    def height(self, node):
        root = node
        if not root:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def count_using_stack(self):
        if not self.root:
            return 0
        my_stack = Stack()
        my_stack.push(self.root)
        count = 1
        while not my_stack.isEmpty():
            node = my_stack.top()
            my_stack.pop()
            if node.left:
                count += 1
                my_stack.push(node.left)
            if node.right:
                count += 1
                my_stack.push(node.right)
        return count


def fib(n):
    my_list = [0,1]
    if n < 2:
        return my_list[n]
    for i in range(2,n+1):
        my_list.append( my_list[i-1] + my_list[i-2] )
    return my_list[-1]

print(fib(100))

def test_tree():
    #root = Node(8)
    #tree_1 = Binary_Tree(root)
    #node_1 = Node(9)
    #node_2 = Node(1)
    #node_3 = Node(5)
    #root.left = node_1
    #root.right = node_2
    #root.left.left = node_3
    #result = ""
    #print(tree_1.pre_order_print(tree_1.root))
    #print(tree_1.in_order_print(tree_1.root))
    #print(tree_1.count())
    root = Node(8)
    tree_2 = Binary_Tree(root)
    root.left = Node(3)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right = Node(10)
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    print(tree_2.pre_order_print(tree_2.root))
    #print(tree_2.count())
    #print(tree_2.height(tree_2.root))
    #print(tree_2.count_using_stack())
    #print(tree_2.pre_order_stack_print())
    #print(tree_2.in_order_stack_print())
    #print(tree_2.post_order_stack_print())
    #print(tree_2.post_order_stack_print_2())
    root_3 = Node(1)
    tree_3 = Binary_Tree(root_3)
    root_3.left = Node(2)
    root_3.right = Node(3)
    root_3.left.left = Node(4)
    root_3.left.right = Node(5)
    root_3.right.left = Node(6)
    root_3.right.right = Node(7)
    #print(tree_3.post_order_stack_print_2())
    print(tree_2.post_order_stack_print_3())
    print(tree_2.level_print())
    print(tree_2.in_order_print(root))
    print(tree_2.height(tree_2.root))

#test_tree()

