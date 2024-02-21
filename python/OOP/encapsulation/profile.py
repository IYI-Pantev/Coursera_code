# class Profile:
#     name_min_length = 3
#     password_min_length = 4
#     def __init__(self, username, password) -> None:
#         self.username = username

#     @property
#     def username(self):
#         return self.__username
    
#     @username.setter
#     def username(self, usnm):
#         if len(usnm) <= self.name_min_length:
#             raise ValueError(f'name must be more than {Profile.name_min_length} characters long.')
#         self.__username = usnm
    
# jsn = Profile('jsn_z', 124124)

# print(jsn.username)

class Profile:
    name_min_length = 3
    password_min_length = 4
    def __init__(self, username, password) -> None:
        self.set_username(username)
        self.set_password(password)

    def get_username(self):
        return self.__username
    
    def set_username(self, usnm):
        if len(usnm) <= self.name_min_length:
            raise ValueError(f'name must be more than {Profile.name_min_length} characters long.')
        self.__username = usnm
    
    def get_password(self):
        return len(str(self.__password)) * '*'
    
    def set_password(self, pwd):
        if len(str(pwd)) <= self.password_min_length:
            raise ValueError(f'password must be more than {Profile.password_min_length} characters long.')
        self.__password = pwd
    
jsn = Profile('jsn_z', 124124)

print(jsn.get_username())

print(jsn.get_password())
jsn.set_password(12345)

#print(jsn.password)