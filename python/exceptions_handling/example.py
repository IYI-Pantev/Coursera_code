def devide_by(a, b):
    return a / b

try:
    ans = devide_by(40, 0)
    print(ans)
# except Exception as e:
#     print("you can not", e)
#     print(e.__class__)
except ZeroDivisionError as e:
    print(e, '[we cannot devide by zero]')
except Exception as e:
    print(e, 'some error except zero devision error')

