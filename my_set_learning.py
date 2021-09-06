#### SET: unordered, unique, unchangeable

def my_set_test():
    my_set = {1, 2, 3, 4, 5, 6, 7, 8}
    my_set.remove(1)
    my_set.discard(0)
    my_set.add(10)
    my_set.update([20, 30])
    my_set.clear()
    print(my_set)

def my_set_test2():
    my_set = {1, 10, 10, 100}
    my_list = list(my_set)
    print(my_list)

    my_set2 = set(my_list)
    print(my_set2)

def has_duplicate_element(l):
    test_set = set(l)
    return len(l) > len(test_set)
    """if len(l) > len(test_set):
        return True
    else:
        return False"""

def test_3():
    example_list = [1, 2, 3, 4]
    print(has_duplicate_element(example_list))

def my_intersection():
    set_1 = {1, 2, 3}
    set_2 = {1, 2, 4, 5}
    #set_3 = set_1.intersection(set_2)
    set_3 = set_1.union(set_2)
    return set_3

def test_4():
    print(my_intersection())








if __name__ == '__main__':
    #my_set_test2()
    test_4()
