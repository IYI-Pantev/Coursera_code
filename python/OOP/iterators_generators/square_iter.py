class SquaresIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration  # StopIteration to signal the end of iteration

# Using the iterator
squares_iter = SquaresIterator(5)

# Iterating using a for loop
for square in squares_iter:
    print(square)
# Output:
# 1
# 4
# 9
# 16
# 25

#You can also use the iter() and next()
#functions to manually iterate over the elements:
    
iterator = iter(squares_iter)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 4
print(next(iterator))  # Output: 9