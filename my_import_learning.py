#from my_class_learning import matrix as mc
import time as mytime
import random
import math

"""def test():
    
    c1 = mc([[1,2],[3,4]])
    c2 = mc([[6,7],[9,0]])
    c1.add_matrix(c2)
    for i in range(2):
        print(c1.get_row(i))
    start_time = mytime.time()
    print(start_time)
    for i in range(1000000):
        print(random.randint(0,100000))
    end_time = mytime.time()
    print(end_time - start_time)
"""
alpha_ = "abcdefghijklmnopqrstuvwxyz"
def generate_one_string():
    my_str = ""
    for i in range(10):
        my_index = random.randint(0,25)
        my_str += alpha_[my_index]
    return my_str

def test():
    for i in range(10000):
        print(generate_one_string())
if __name__ == '__main__':
    test()



# def a function generate 10000 points object, x in range(-100, 100), same range for y
# ? find two points which have the largest distance, also find the closest two points ?
def find_two_points():
    point = []
    point_list = []
    for i in range(10000):
        j = 0
        while j <=1:
            point.append(random.uniform(-100,100))
            j+=1
        point_list.append(point)
    min_dist = 100
    closest_pair = []
    for x in range(len(point_list)):
        y = x + 1
        while y <= len(point_list):
            if math.sqrt(pow(point_list[x][0]-point_list[y][0],2)+pow(point_list[x][1]-point_list[y][1],2)) <= min_dist:
                min_dist = math.sqrt(pow(point_list[x][0]-point_list[y][0],2)+pow(point_list[x][1]-point_list[y][1],2))
                closest_pair = [x , y]
                y += 1
            else:
                y += 1
    max_dist = 0
    furtherest_pair = []
    for p in range(len(point_list)):
        q = p + 1
        while q <= len(point_list):
            if math.sqrt(pow(point_list[p][0]-point_list[q][0],2)+pow(point_list[p][1]-point_list[q][1],2)) <= min_dist:
                min_dist = math.sqrt(pow(point_list[p][0]-point_list[q][0],2)+pow(point_list[p][1]-point_list[q][1],2))
                closest_pair = [p , q]
                q += 1
            else:
                q += 1
    return [min_dist, closest_pair, max_dist, furtherest_pair]



