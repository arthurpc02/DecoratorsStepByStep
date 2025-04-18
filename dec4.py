from time import time

""" We use a function that returns a wrapper function.
In Summary, timer() function wraps add() or sub() function
with the time measurement functionality. """

def timer(func):
    def wrapper_function(x,y=10):
        before = time()
        rv = func(x, y)
        after = time()
        print(f"took {after - before} seconds to run.")
        return rv
    return wrapper_function

def add(x,y=10):
    return x + y
add = timer(add)

print(add(20,30))
print(add(2,3))





