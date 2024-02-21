import sys

x = 1
print("The memory address of x is", hex(id(x)))
print("The size of x is", sys.getsizeof(x), "bytes")
def f():
    global x
    print(x)
    x = 2
f()
print(x)
print("The memory address of x is", hex(id(x)))

