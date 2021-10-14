from my_class_learning import matrix as mc
import time as mytime
import random

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
