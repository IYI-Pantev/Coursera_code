import time


def my_generator(n):
    for i in range(n):
        print(f"Before yield: {i}")
        yield i
        print(f"After yield: {i}")

for i in my_generator(5):
    time.sleep(1)
