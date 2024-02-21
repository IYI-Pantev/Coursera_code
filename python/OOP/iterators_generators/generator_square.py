def generate_squares(limit):
    current = 1
    while current <= limit:
        yield current ** 2
        current += 1

# Using the generator
squares_gen = generate_squares(5)

# Iterating using a for loop
for square in squares_gen:
    print(square)
# Output:
# 1
# 4
# 9
# 16
# 25
squares = generate_squares(4)
print(next(squares))
print(next(squares))
print(next(squares))