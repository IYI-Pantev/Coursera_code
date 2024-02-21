# define a class Person
class Person:
    # initialize the class with a name parameter
    def __init__(self, name):
        self.name = name
    
    # define a method to return an iterator object for the name
    def __iter__(self):
        return iter(self.name)

# create an instance of Person with a name
p = Person("Alice")

# iterate through the name
# for letter in p:
#     print(letter)

# using next
print(next(p))