import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("Time:", total)
        return rv

    return wrapper

# how to implement a simple decorator
@timer
def test():
    for _ in range(100000):
        pass


test()
