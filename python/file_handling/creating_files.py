try:
    with open('python/file_handling/newfile', 'a') as file:
        file.writelines('\nthis is appended line')
except FileNotFoundError as e:
    print("ERROR" , e)
