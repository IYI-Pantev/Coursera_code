# sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
# print(sample_dict[1])
# sample_dict[2] = 'Mint Tea'
# print(sample_dict)
# del sample_dict[3]
# print(sample_dict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
# The list of the keys is a view of the dictionary,
# meaning that any changes done to the dictionary
# will be reflected in the keys list.
for key in thisdict.keys():
    print(key)
print('- - - - - -')
for k, v in thisdict.items():
    print(f'|{k} : {v}|')


