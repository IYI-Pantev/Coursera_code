def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        upper_case = result.upper()
        return upper_case
    return wrapper
@uppercase # easier way to apply decorator
def reverser(name):
    return name[::-1]

# uprc = uppercase(reverser)
# print(uprc('kcin'))
print(reverser("kcilc"))