def listFunc():
    mylist = [1, 2, 3, 4, 5, 6, 7]
    print(mylist)
    #how to detect empty list
    if len(mylist) == 0:
        print('empty list')
    else:
        print("nonempty")

    #print(mylist[0])
    #print(mylist[len(mylist)-1])
    list_len = len(mylist)
    for i in range(list_len):
        print(mylist[list_len-1-i]*2)

    for x in mylist:
        print(x*2)

    print(mylist[0:5])

    for i in range(list_len):
        if i % 2 == 0:
            mylist[i] += 5
    print(mylist)


    max_num = mylist[0]
    for i in range(1, list_len):
        if mylist[i] > max_num:
            max_num = mylist[i]
    print(max_num)

    print(min(mylist))

    """mylist.insert(2, 19)
    print(mylist)

    mylist.remove(19)
    print(mylist)

    mylist.pop()
    print(mylist)

    mylist.pop(-2)
    print(mylist)

    mylist.clear()
    print(mylist)"""

    print(mylist.count(6))



def find_most_freq_element(l):
    result_l = []
    for x in l:
        result_l.append(l.count(x))
    return max(result_l)

def test():
    example_list = [3, 0, 9191, 2, 2, 2]
    print('print result')
    print(find_most_freq_element(example_list))
    example_list.sort(reverse=True)
    print(example_list)
    example_list.reverse()
    print(example_list)

    new_list = sorted(example_list)
    print(new_list)
    print(example_list)
    example_list.sort()
    print(example_list)

def my_reverse_list(l):
    result_list = []
    for i in range(len(l)):
        result_list.append(l[len(l)-1-i])
    return result_list

def test_2():
    example_list = [1, 1, 3, 4, 5]
    #print(my_reverse_list(example_list))
    example_list.remove(1)
    print(example_list)

def my_min(mylist):
    min_num = mylist[0]
    for i in range(1, len(mylist)):
        if mylist[i] < min_num:
            min_num = mylist[i]
    return min_num

def my_sort(l):
    result_list = []
    while len(l) > 0:
        min_val = my_min(l)
        result_list.append(min_val)
        l.remove(min_val)
    return result_list

def test_3():
    example_list = [1, 8, 10, 2, 7]
    print(my_sort(example_list))


def my_reverse_2(l):
    for i in range(int(len(l)/2)):
        # i swap len(l)-1-i
        temp = l[i]
        l[i] = l[len(l)-1-i]
        l[len(l)-1-i] = temp
    return l

def test_4():
    new_list = [1, 2, 3, 4]
    print(my_reverse_2(new_list))



"""def my_swap(x, y):
    tmp = x
    x = y
    y = tmp
    #return [x, y]

def test_4():
    m = 3
    n = 9
    my_swap(m, n)
    print('m swap n')
    #print(my_swap(x, y))
    print(m)
    print(n)"""


if __name__ == '__main__':
    #listFunc()
    #test()
    #my_reverse_list()
    #test_2()
    #test_3()
    test_4()
