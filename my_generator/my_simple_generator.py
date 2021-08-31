import sys

"""
    Generators are  expert feature of python,
        They help's us to deal better with the
        computers RAM memory.

    Tips:   yield => pause
            return => stop
"""


def gen(n):
    for i in range(n):
        yield i ** 3


x = [i ** 2 for i in range(10000)]
g = gen(100000)


print(sys.getsizeof(x))
print(sys.getsizeof(g))


"""
for i in g:
    print(i)
"""
