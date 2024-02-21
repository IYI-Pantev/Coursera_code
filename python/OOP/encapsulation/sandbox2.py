class Profile:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
    
    def full_name(self):
        return f"{self.first} {self.last}"
    

emp_1 = Profile('nick', 'buster')

print(emp_1.email)

