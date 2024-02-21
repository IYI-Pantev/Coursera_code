# first way
# file = open('python/file_handling/test.txt', mode = 'r')

# data = file.readline()
# print(data)

# file.close

with open('python/file_handling/test.txt', 'r') as file:
    data = file.readline()

    print(data)