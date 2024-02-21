# pure funcions does not change or alter the input data or data out of the scope

# example of traditional function
my_list = [1, 2 ,3]

# def add_to(item):
#     return my_list.append(item)

# add_to(4)
# print(my_list)

# pure function
def add_to(lst, item):
    new_list = lst.copy()

    new_list.append(item)

    return new_list


print(my_list)
print('_-_-_')
print(add_to(my_list, 4))