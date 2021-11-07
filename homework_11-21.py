#  globals().clear()

s = "}"
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

print(my_leetcode_20_2(s))
