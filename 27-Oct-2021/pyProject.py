# projects 
# ------------
# ex1
# ------------
#  Write a Python program to create all possible strings 
#  by using 'a', 'e', 'i', 'o', 'u'. 
# Use the characters exactly once.

# solution

# 
import random
char_list = ['a', 'e', 'i', 'o', 'u']
random.shuffle(char_list)
print(''.join(char_list))
import string

#  Write a Python program to get all possible two digit 
# letter combinations from a digit (1 to 9) string
def letter_combinations(digits):
    if digits == "":
        return []
    string_maps = {
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tuv",
        "8": "wxy",
        "9": "z"
    }
    result = [""]
    for num in digits:
        temp = []
        for an in result:
            for char in string_maps[num]:
                temp.append(an + char)
        result = temp
    return result

digit_string = "47"
print(letter_combinations(digit_string))
digit_string = "29"
print(letter_combinations(digit_string))