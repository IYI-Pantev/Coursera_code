def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
    
text = 'reversal'
print(string_reverse(text))