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

def merge_two_list(l1,l2):
    if not l1:
        return l2
    if not l2:
        return l1
    result = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    if i < len(l1):
        result.extend(l1[ i:len(l1) ])
    if j < len(l2):
        result.extend(l2[ j:len(l2) ])
    print('result:',result)
    return result




def merge_sort(l):
    if len(l) < 2:
        return l
    mid_idx = int(len(l)/2)
    l1 = l[:mid_idx]
    l2 = l[mid_idx:]
    print('l1:',l1)
    print('l2:', l2)
    print('-'*10)
    merge_sort(l1)
    merge_sort(l2)
    #return merge_two_list(l1_sorted, l2_sorted)
    i = j = k = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l[k] = l1[i]
            i += 1
        else:
            l[k] = l2[j]
            j += 1
        k += 1

    while i < len(l1):
        l[k] = l1[i]
        i += 1
        k += 1
    while j < len(l2):
        l[k] = l2[j]
        j += 1
        k += 1
    print('l', l)

#leetcode 148
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mid_node(self, node):
        if not node:
            return None
        if not node.next:
            return node
        count = 0
        curr_node = node
        while curr_node:
            count += 1
            curr_node = curr_node.next
        mid = (count-1)//2
        curr_node = node
        while mid > 0:
            curr_node = node.next
            mid -= 1
        return curr_node

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        left = head
        mid = self.mid_node(left)
        right = mid.next
        mid.next = None
        l1 = self.sortList(left)
        l2 = self.sortList(right)

        curr_l1 = l1
        curr_l2 = l2
        result = ListNode(0)
        new_head = result
        while curr_l1 and curr_l2:
            if curr_l1.val < curr_l2.val:
                result.next = curr_l1
                curr_l1 = curr_l1.next
            else:
                result.next = curr_l2
                curr_l2 = curr_l2.next
            result = result.next
        if curr_l1:
            result.next = curr_l1
        if curr_l2:
            result.next = curr_l2
        return new_head.next

    def print(self,head):
        if not head:
            return None
        curr_node = head
        my_list = []
        while curr_node:
            my_list.append(curr_node.val)
            curr_node = curr_node.next
        print(my_list)

import heapq

class Max_Heap():
    def __init__(self):
        self.heap_list = []

    def __str__(self):
        s = "this is my heap list:" + str(self.heap_list)
        return s

    def get_max(self):
        if self.heap_list:
            return self.heap_list[0]
        else:
            return None

    def siftup(self, idx):
        parent_idx = (idx-1)//2
        if parent_idx < 0:
            return
        tmp = self.heap_list[parent_idx]
        if tmp < self.heap_list[idx]:
            self.heap_list[parent_idx] = self.heap_list[idx]
            self.heap_list[idx] = tmp
            self.siftup(parent_idx)

    def insert(self, value):
        self.heap_list.append(value)
        self.siftup(len(self.heap_list)-1)

    def siftdown(self, idx):
        left_child = idx*2 + 1
        right_child = idx*2 + 2
        largest_idx = idx
        if len(self.heap_list) > left_child and self.heap_list[left_child] > self.heap_list[largest_idx]:
            largest_idx = left_child
        if len(self.heap_list) > right_child and self.heap_list[right_child] > self.heap_list[largest_idx]:
            largest_idx = right_child
        if largest_idx != idx:
            self.heap_list[largest_idx], self.heap_list[idx] = \
                self.heap_list[idx], self.heap_list[largest_idx]
            self.siftdown(largest_idx)

    def remove_max(self):
        if not self.heap_list:
            return None
        """if len(self.heap_list) == 1:
            value = self.heap_list[0]
            self.heap_list.pop()
            return value"""
        max_value = self.heap_list[0]
        self.heap_list[0] = self.heap_list[-1]
        self.heap_list.pop()
        self.siftdown(0)
        return max_value

    def sort(self):
        my_list = []
        #target = self.heap_list
        value = self.remove_max()
        while value:
            my_list.append(value)
            value = self.remove_max()
        return my_list

def test():
    x=[2,7,3,6,4,12,5]
    y1 = [4,7,9]
    y2 = [2,3,6]
    #head = ListNode(4)
    #head.next = ListNode(2)
    #head.next.next = ListNode(1)
    #head.next.next.next = ListNode(3)
    #print(helper(x,0,len(x)-1))
    #print(x)
    #print(quick_sort(x,0,len(x)-1))
    #print(x)
    #print(naive_sorting(x))
    #print(merge_two_list(y1,y2))
    #merge_sort(x)
    #print(x)
    #leetcode148 = Solution()
    #leetcode148.print(head)
    #leetcode148.sortList(head)
    my_heap = Max_Heap()
    #print(my_heap.get_max())
    li = [5, 7, 9, 1, 3]
    for x in li:
        my_heap.insert(x)
    print(my_heap)
    print(my_heap.sort())
    heapq.heapify(li)
    print(li)
    heapq.heappush(li, 0 )
    print(li)
    heapq.heappop(li)
    print(li)
    print(heapq.nlargest(3, li))
    print(heapq.nsmallest(3, li))





test()



