def my_function(n):
    n *= 2
    return n

def my_f_2():
    p = my_function
    print(p(10))

x = lambda a,b:a+b

def my_lambda():
    print(x(100,12))

my_dict = {1:-100, 2:4, 3:-20}


def my_sorted(item):
    return abs(item[1])

def sort_dict(dict):
    #print(sorted(dict.items(), key = lambda a:abs(a[1])))
    print(sorted(dict.items(), key= my_sorted))


if __name__ == '__main__':
    #my_f_2()
    #my_lambda()
    sort_dict(my_dict)
