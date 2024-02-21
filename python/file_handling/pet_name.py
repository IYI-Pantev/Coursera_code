import random
with open('python/file_handling/pet_names.txt', 'r') as data:
    names = data.read()
    n_list = names.split('\n')
    
    print(random.choice(n_list))