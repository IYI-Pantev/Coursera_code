file = open('python/file_handling/crsr.txt', 'r')

data = [s for s in file if not s[0] == " "]
reversed_data = data[::-1]
print(reversed_data)
#for s in file:
 #   print(s)
print(data)
e = enumerate(data)
print(e)
evens = [s for n, s in e if not n % 2 == 0]


print(evens)
#print(file.read())
# t = file.read()
# print(t)
# o = t.split("\n")
# print(o)
file.close()