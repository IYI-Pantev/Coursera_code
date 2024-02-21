def my_generator(n):
    # initialize counter
    value = 0
    # loop until counter is less than n
    while value < n:
        # produce the current value of the counter
        yield value
        # increment the counter
        value += 1

# create a generator object from the generator function
generator = my_generator(3)

# iterate over the generator object and print each value
for i in range(10):
    try:
        print(next(generator))
    except StopIteration:
        print('generator depleted')
        break
