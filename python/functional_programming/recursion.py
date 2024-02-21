# iterative 
# def walk(steps):
#     for step in range(1, steps + 1):
#         print(f'you take step #{step}')


# walk(13)

# recursive

def walk(steps):
    if steps == 0:
        return
    walk(steps - 1) # it makes a stack and starts from the last one after the base condtition is met
    print(f"you take step #{steps}")

walk(13)

def sum(n):
   if n == 1:
       return 0
   return n + sum(n-1)

a = sum(5)
print(a)