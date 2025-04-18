from time import time

""" We write a timer() function that takes add()
or sub() function as argument. It works, but we have
to call timer(func) everytime we execute any of those
functions. """

def timer(func, x, y):
    before = time()
    rv = func(x, y)
    after = time()
    print(f"took {after - before} seconds to run.")
    return rv

def add(x,y=10):
    return x + y

print(timer(add,20,30))
print(timer(add,2,3))




