from time import time

""" Wrap the time measurement inside the add()
function. It improves, but if we add a new
sub() function, we would have to rewrite it."""

def add(x,y=10):
    before = time()
    rv = x + y
    after = time()
    print(f"took {after - before} seconds to run.")
    return rv

print(add(20,30))
print(add(2,3))




