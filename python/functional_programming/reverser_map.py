# str[start:stop:step]
trial = 'reversal'
new_trial = trial[1:6]
print(new_trial)
coffees = ['Espresso', 'Latte', 'Capuccino', 'Macchiato', 'Americano', 'Decaf']

def reverser(str):
    return str[::-1]

reversed_coffees = map(reverser, coffees)

print(*reversed_coffees)