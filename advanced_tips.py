# list comprehension
from functools import reduce
import re
def practice_1(l):
    my_list = []
    for i, e in enumerate(l):
        if i % 2 == 0:
            my_list.append(e*2)
        else:
            my_list.append(e+10)
    return my_list


#print(practice_1([1, 2, 3, 4, 5, 6, 7, 8, 9]))
def map_reduce(s):
    my_map = {}
    my_map['0'] = 0
    my_map['1'] = 1
    my_map['2'] = 2
    my_map['3'] = 3
    my_map['4'] = 4
    my_map['5'] = 5
    my_map['6'] = 6
    my_map['7'] = 7
    my_map['8'] = 8
    my_map['9'] = 9
    my_res = reduce(lambda x,y: 10*x + y, map(lambda x: my_map[x], s))
    return my_res


#print(map_reduce("12356"))

def practice_2(s):
    my_filter = filter(lambda x: x.isalpha(), s)
    my_map = map(lambda x: x.lower(), my_filter)
    my_reduce = reduce(lambda x,y: x + y, my_map)
    return my_reduce


#print("".join(practice_2("ARCHER193&*%()")))
#print(practice_2("ARCHER193&*%()"))
def practice_3():
    my_file = open("install.log", "r")
    content = my_file.read()
    content_list = content.split('\n')

    #for i, cont in enumerate(content_list):
        #print(i,cont)
    #my_filter = filter(lambda x: "system" in x, content_list)
    #content_wth_system = list(my_filter)
    for i, x in enumerate(content_list):
        z = re.search(r"[Ss][Oo].*\d{5}]:", x)
        #print(x)
        if z:
            print(i, x)

practice_3()
