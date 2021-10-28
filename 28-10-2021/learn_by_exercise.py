# ------------------------
# LEARN BY EXERCISE ------
# ------------------------
# write python program can remove specific character from string
import string
# def removecharstr(stringchar1="", char_to_be_removed=""):
#     for i in stringchar1:
#         if i == char_to_be_removed:
#             stringchar1.remove(i)
#         else:
#             print(f"The {stringchar1} has no character of {char_to_be_removed}")
#     print(stringchar1)
# # removecharstr("asahmed", 'q')

# removecharstr("asahmed", 'a')
# anothor solution
def remove_characters(str1,c):
    return ''.join([el for el in str1 if el == c])
print(remove_characters("asahmed", 'h'))