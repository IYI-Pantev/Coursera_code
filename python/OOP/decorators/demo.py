def f(x):
    def internal_f(y):
        return x + y
    internal_f.initial_value = x
    return internal_f

f1 = f(1)(2) # two calls for the outer and internal func
print(f1)
# print(f1(2))
# print(f1.initial_value)