# Example Multiple Inheritance
class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)

# example Multi-level inheritance
class D:
   a = 1

class E(D):
   a = 2

class F(E):
   pass
f = F()
print(f.a)

# example Built-in functions issubclass() and isinstance()
print(issubclass(C,A))

print(isinstance(f, F))

# example super() function