### Function a block of code implement some functionality, callable

def my_first_function(*parameter_1):
    my_list = list(parameter_1[0])
    my_list.pop()
    print(my_list)
    #print(parameter_2)
    #print(parameter_3)

#default parameter follows non-default parameter when creating functions
def my_funciton_2(p1, p2, p3, p4="tom"):
    #my_list = [p1, p2, p3]
    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)
    print("p4:", p4)

def my_print():
    print("this is my print funciton")

def my_function_3(parameter):
    if isinstance(parameter, list):
        print(sorted(parameter))
    else:
        my_print()

# recursion function
def my_recursive(n):
    if n == 1:
        return 1
    else:
        return n * my_recursive(n-1)



def my_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return my_fibonacci(n-1) + my_fibonacci(n-2)

def my_print_fibo(n):
    for i in range(n):
        print(my_fibonacci(i))


"""Leet Code Q66"""
def plusOne(digits):
    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    else:
        digits.pop()
        new_list = plusOne(digits)
        new_list.append(0)
        return new_list


def recursive_reverse_list(l, i=0):
    if i > int(len(l)/2):
        return l
    else:
        temp_value = l[i]
        l[i] = l[-(i+1)]
        l[-(i+1)] = temp_value
        new_list = recursive_reverse_list(l, i+1)
        return new_list


def test_1():
    my_list = [1, 2, 3, 4, 5]
    print(recursive_reverse_list(my_list, 0))


def max_list(l):
    if len(l) == 1:
        return l[0]
    else:
        if l[0] > max_list(l[1:]):
            return l[0]
        else:
            return max_list(l[1:])


def recursive_2(l):
    if len(l) < 2:
        return l
    else:
        l2 = l[1:-1]
        print("12,", 12)
        l3 = recursive_reverse_list(l2)
        print("l3", l3)
        la = []
        la.append(l[-1])
        la.extend(l3)
        la.append(l[0])
        print("la,", la)
        return la





if __name__ == '__main__':
    #my_first_function([1, 2, 3, 4], [1,2], ("H","L"))
    #print(my_funciton_2(-1, 100, 2))
    #my_funciton_2(-1, 100, 2, "jack")
    #my_function_3((1, 100, 2))
    #print(my_recursive(3))
    #print(my_fibonacci(10))
    #print(my_print_fibo(100))
    #print(plusOne([8, 9, 9, 9]))
    test_1()
