# coding: utf-8
def is_palindrome(s):
    test = {}
    for char in s.lower():
        if char.isalpha():
            test[char] = test.get(char, 0) + 1
    
    allowed = True  # One value can be an odd number if s is not an even string
    print test
    for value in test.values():
        if value % 2 != 0:
            if allowed:
                allowed = False
            else:
                return False
   
    return True
