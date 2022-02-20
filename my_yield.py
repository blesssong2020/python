# decorator
import time
import logging
import logging.config

def compute_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print("time used:",start_time - end_time)
    return wrapper

@compute_time
def foo():
    #print(list1)
    #print(list2)
    logging.basicConfig(filename= "example.log",
                        format='%(asctime)s - %(message)s',
                        level=logging.INFO,
                        datefmt='%d-%b-%y %H:%M:%S')
    logging.warning("function name %s", foo.__name__)
#foo = compute_time(foo) <=> decorator

@compute_time
def my_function(*args):
    for x in args:
        print(x)
@compute_time
def my_function_2(*args,**kwargs):
    for y in args:
        print(y)
    for _, x in kwargs.items():
        print(x)




def test():
    #my_function(1,3,["string"])
    list1 = [1,2,3]
    list2 = ["a","n"]
    #foo(list1,list2)
    my_function_2(list1, list2, name = "Archer", number = 7)








""""@compute_time
def isa_prime():
    for x in range(2, 10000):
        flag = True
        for i in range(2, x):
            if x % i == 0:
                flag = False
                break
        if flag:
            print(x, "is prime")
@compute_time
def add_sum():
    start_time = time.time()
    res = 0
    for i in range(10**5):
        res += i
    print("sum",res)
    end_time = time.time()
    print(start_time - end_time, "time used")


#isa_prime()
#add_sum()
def test_exception():
    try:
        print(1/1)
        raise ValueError('valueE class')
    except EnvironmentError as x:
        print(x)
    except:
        print("something wrong")
        raise ValueError ("new value Error")
    return
    else:
        pass
    finally:
        print("program exit")
def test_2():
    try:
        test_exception()
    except:
        print("y")
test_2()"""

class myDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        self.func(*args,**kwargs)
        end_time = time.time()
        print("time used:",start_time - end_time)


@myDecorator
def print_func():
    print("my original function")

#print_func = myDecorator(print_func) => class decorator
print_func()


class my_call:
    def __init__(self):
        pass
    def __call__(self,*args,**kwargs):
        for x in args:
            print(x)
        for  _,y in kwargs.items():
            print(y)
        print("this is call function")

example1 = my_call()
example1(1,"archer",name="archer")


