#iterator
#iterable for in
from collections.abc import Iterable



def number_gen(n):
    for x in range(n):
        yield x

    yield 3
    yield 5
    yield 1
    yield 100
    yield 8
    print("number gen is done")

g = number_gen(5)

while True:
    try:
        print(next(g))
    except StopIteration:
        print("out of scope")
        break

def foo():
    list = []
    for i in range(1,10):
        list.append(i)
    return list
