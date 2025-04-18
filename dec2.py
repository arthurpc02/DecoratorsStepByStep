from time import time

def add(x,y=10):
    before = time()
    rv = x + y
    after = time()
    print(f"took {after - before} seconds to run.")
    return rv

print(add(20,30))
print(add(2,3))




