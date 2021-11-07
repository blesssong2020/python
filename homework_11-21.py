#  globals().clear()

s = "([])"
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

print(leetcode_20(s))

