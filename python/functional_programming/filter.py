menu = ['espresso', 'mocha', 'latte', 'cappuccino', 'cortado', 'americano']

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee
    
searched = map(find_coffee, menu)
print(*searched)

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x >= 18:
    return x
#   if x < 18:
# #     return False
# #   else:
# #     return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)
