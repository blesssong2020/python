#
import random
import time as mytime
"""
my_list = []
random.seed(999)
number = 10**5
for x in range(number):
    my_list.append(random.randint(-100*number,100*number))

target = my_list[999]
print(target)
my_list.sort()
#print(my_list)

def find_idx(list, target):
    start_time = mytime.time()
    for i in range(len(list)):
        if list[i] == target:
            end_time = mytime.time()
            print("search time:", end_time - start_time)
            return i
    end_time = mytime.time()
    print("search time", end_time-start_time)
    return -1

def quick_find_recursive(list, target):
    def helper(list, low, high, target):
        if low > high:
            return -1

        if low == high:
            if target == list[low]:
                return low
            else:
                return -1

        mid = int( (high + low)/2 )

        if target == list[mid]:
            return mid
        if target < list[mid]:
            return helper(list, low, mid, target)
        else:
            return helper(list, mid, high, target)

    return helper(list, 0, len(list)-1, target, 0)

def quick_find(list, target):
    def helper(list, low, high, target):
        while low <= high:
            mid = int( (high + low)/2 )

            if target == list[mid]:
                return mid
            if target < list[mid]:
                high = mid
            else:
                low = mid
        return -1
    return helper(list, 0, len(list)-1, target)

print(my_list[find_idx(my_list,target)]==target)
start_time = mytime.time()
print(my_list[quick_find(my_list, target)]==target)
end_time = mytime.time()
print(quick_find(my_list,target))
print("search time 2", end_time-start_time)"""

# quick sort
# time complexity O(n^2)
def naive_sorting(list):

    def helper(list):
        min_val = min(list)
        list.remove(min_val)
        return [min_val,list]
    result = []
    while list:
        print(list)
        result.append(helper(list)[0])
    return result

def helper(list, low, high):
    pivot = list[high]
    i = low-1
    for j in range(low,high):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[high] = list[high], list[i+1]
    print("helper over", list, i+1)
    return i+1

def quick_sort(list, low, high):
    if len(list) == 1:
        return
    if low < high:
        position = helper(list, low, high)
        quick_sort(list, low, position-1)
        quick_sort(list, position +1, high)


def test():
    x=[2,7,3,6,4,12,5]
    #print(helper(x,0,len(x)-1))
    #print(x)
    #print(quick_sort(x,0,len(x)-1))
    #print(x)
    print(naive_sorting(x))


test()
