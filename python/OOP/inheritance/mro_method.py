class A:
    pass

class B(A):
    pass

class C(B):
    pass
# gives the path of finding from where inherited method or atribute
print(C.mro()) 
print([cls.__name__ for cls in C.__mro__])
# print('...--------...')
# gives more details
# print(help(C))