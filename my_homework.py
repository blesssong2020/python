import random
import math
random.seed(100)
import time

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def distance(self, other):
        return math.sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))
# def a function generate 10000 points object, x in range(-100, 100), same range for y
# ? find two points which have the largest distance, also find the closest two points ?
def find_two_points():
    t1 = time.time()
    #print(t1)
    point_list = []
    for i in range(10000):
        point = Point(random.uniform(-100,100), random.uniform(-100,100))
        point_list.append(point)
    #min_dist_sq = float('inf')
    min_dist = point_list[0].distance(point_list[1])
    closest_pair = []
    for i in range(len(point_list)-1):
        j = i + 1
        while j < len(point_list):
            if abs(point_list[i].get_x()-point_list[j].get_x()) > min_dist or \
                    abs(point_list[i].get_y()-point_list[j].get_y()) > min_dist:
                pass
            elif point_list[i].distance(point_list[j]) < min_dist:
                min_dist = point_list[i].distance(point_list[j])
                closest_pair = [i, j]
            #if point_list[i].distance_sq(point_list[j]) < min_dist_sq:
            #    min_dist_sq = point_list[i].distance_sq(point_list[j])
            #    closest_pair = [i , j]
            j += 1
    t2 = time.time()
    print("execution time:", t2 - t1)
    return [min_dist, point_list[closest_pair[0]], point_list[closest_pair[1]]]


"""
def my_leetcode_39(candidates, target):
    candidates.sort()
    divisor_list = []
    for x in candidates:
        divisor_list.append(int(target/x))

    for i in range(len(candidates)):
        j = 0
        for j in range(len(divisor_list)):
            p = 0
            while p <= divisor_list[j]:

"""


if __name__ == '__main__':
    find_two_points()
    #print(test())

