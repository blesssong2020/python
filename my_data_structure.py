#
import random
import time
from collections import deque

#random.seed(9)
def generate_int():
    count = 0
    my_list = []
    while count < 50000:
        data = random.uniform(0, 1000000)
        my_list.append(data)
        count += 1
    return my_list

def find_kth_largest(l, k):
    t_1 = time.time()
    l.sort(reverse=True)
    if k <= len(l):
        t_2  = time.time()
        print("execution time:", t_2-t_1)
        return l[k-1]
    else:
        return k[0]

def find_k_second_attempt(l, k):
    t1 = time.time()
    k_list = l[0:k]
    k_list.sort(reverse=True)
    for i in range(k,len(l)):
        k_list = process_current_value(k_list, l[i])
    t2 = time.time()
    print("second time:", t2-t1)
    return k_list[-1]

def process_current_value(k_list, value):
    if value > k_list[-1]:
        k_list[-1] = value
        k_list.sort(reverse=True)

    return k_list

def test():
    data = generate_int()
    #data.sort(reverse=True)
    #print(data)
    #print(find_k_second_attempt(data, 5))
    print(find_kth_largest(data, 5))

def test_stack():
    stack = [3,4,5]




if __name__ == "__main__":
    test()
