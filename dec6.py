from time import time

""" We can improve the decorator by adding
(*args, **kwargs). Now it can take functions
with different argument combinations. """

def timer(func):
    def wrapper_function(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print(f"took {after - before} seconds to run.")
        return rv
    return wrapper_function

@timer
def add(x,y=10):
    return x + y

print(add(20,30))
print(add(2,3))




