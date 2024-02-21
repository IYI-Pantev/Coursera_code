# Algorithm for a Palindrome
import math
def isPalindrome(str):
    
    j = 1
    for i in range(math.floor(len(str)/ 2)):
        
        if str[i] != str[len(str) - j]:
            return False
        j += 1
    return True

print(isPalindrome('racecar'))

