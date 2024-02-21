list1 = [1, 2, 3, 4, 5]

# print unpacking
print(*list1)

# second way
print(list1, end = '')
print()

# insert 
list1.insert(len(list1), 6)
print(list1)
# append
list1.append(7)
print(list1)
# extend
list1.extend([8, 9])
print(list1)
#pop
list1.pop(4)
print(list1)
#del
del list1[3]
print(list1)
