import random
import math
random.seed(100)
import time
import numpy as np
import statistics as st

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






def helper(candidates, target):
    print(type(candidates))

    if not candidates:
        return []

    if target <= 0:
        return []

    if target < candidates[0]:
        return []

    if target == candidates[0] and len(candidates) == 1:
        tmp = []
        tmp.append(candidates)
        return tmp

    results = []
    val = candidates[0]
    loop = 0
    count = int(target/val)
    candidates.pop(0)

    while loop <= count:
        results = helper(candidates, target-val*loop)
        print("results", results)

        for x in results:
            for i in range(loop):
                x.append(val)
        print("results 2", results)

        loop += 1
    return results

def combinationSum(candidates, target):
    candidates.sort()
    return helper(candidates, target)

def leetcode_39_test():
    l = [3,4,5]
    target = 10
    combinationSum(l,target)




def my_clustering(k = 4):
    point_list = []
    for i in range(200):
        j = 0
        point = []
        while j <= 1:
            point.append(random.uniform(0, 100))
            j += 1
        point_list.append(point)
    k_points = []
    for i in range(k):
        k_points.append(point_list[random.randint(0, 19)])
    #print("original list:", point_list)
    transpose_k = np.array(k_points).T
    for i in range(len(point_list)):
        distance = ( (transpose_k[0] - point_list[i][0]) ** 2 + (transpose_k[1] - point_list[i][1]) ** 2) ** 0.5
        closest_idx = np.argmin(distance)
        # closest_idx is under class numpy.int64
        point_list[i].append(closest_idx)
    print(point_list)

    #print(k_points)
    loop = 0
    while loop < 100:

        for i in range(len(k_points)):
            x_value = 0
            y_value = 0
            count = 0

            for j in range(len(point_list)):
                if point_list[j][2] == i:
                    x_value += point_list[j][0]
                    y_value += point_list[j][1]
                    count += 1
            if count != 0:
                k_points[i][0] = x_value/count
                k_points[i][1] = y_value/count

        transpose_k = np.array(k_points).T

        for i in range(len(point_list)):
            distance = ( (transpose_k[0] - point_list[i][0]) ** 2 + (transpose_k[1] - point_list[i][1]) ** 2) ** 0.5
            closest_idx = np.argmin(distance)
            # closest_idx is under class numpy.int64
            point_list[i][2] = closest_idx
        loop += 1
        #print(k_points)
    return k_points






if __name__ == '__main__':
    #find_two_points()
    #print(test())
    #leetcode_39_test()
    print(my_clustering())



# Homework, 11/02, debug homework from last week, finish rest of clustering methods, HW-3 file
# using Kmean/svm/naivebayes on text
# HW-4 SVM lDA Topic model


