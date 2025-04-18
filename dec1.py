from time import time

def add(x,y=10):
    return x + y

before = time()
print(add(20,30))
after = time()
print(f"took {after - before} seconds to run.")

before = time()
print(add(2,3))
after = time()
print(f"took {after - before} seconds to run.")



