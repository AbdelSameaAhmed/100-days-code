# ------------
# -- find missing letter
# -----------
# asa ew lhkhs
import string
print(string.ascii_lowercase)
def find_missing_letter_in(givenLetters):
  alpha = string.ascii_lowercase
  start = alpha.index(givenLetters[0])
  for letter in alpha[start:]:
    if letter not in givenLetters:
      return letter
print(find_missing_letter_in("klmlkk,sknbca;jfznopq"))
def longestword(enteredword):
    count = 0
    word_list = enteredword.split(" ")
    for word in word_list:
        if len(word) > count:
            count = len(word)
            longest = word
    return longest
print(longestword("this is the most word unfortuntly itwasthefirstunfor  "))
import string
remove character for mstring
def remove_char_from(word, c):
    stringto =[]
    for char in word:
        if char != c.lower() and char != c.upper():
            stringto.append(char)
    return "".join(stringto)


def remove_char_from(word, c):
    result = filter(lambda x: x != c.upper() and x != c.lower(), word)
    return "".join(result)


print(remove_char_from("ASAD Saysdd ddHello", "d"))
# create function to remove duplicate word from string
print("*"*50)
def remove_dup(sentence):
    words_list = sentence.split(" ")
    result = []
    for word in words_list:
        if word not in result:
            result.append(word)
    return " ".join(result)


def newremove(sentence):
    words_list = sentence.split(" ")
    unique_only = list(dict.fromkeys(words_list))
    final_result = " ".join(unique_only)
    return final_result


# Testing Ouput
print(newremove(" ASA Web Web says Hello "))

print("*" * 50)
print("*" * 50)
print("Format numbers functio")
# formatting numbers functions


def format_numbers(num):
    # Use Commas As Thousands Separator
    num = f"{num:,}"
    # Check If Theres Comma in The Position 4 From The Right
    if (num[-4:-3] == ","):
        # Replace Last Comma With Underscore
        num = f"{num[:-4]}_{num[-3:]}"
    return num


# TEST Function
print(format_numbers(120))  # 120
print(format_numbers(1530))  # 1_530
print(format_numbers(120510650))  # 120,510_650
print(format_numbers(510650480910))  # 510,650,780_910
print(format_numbers(12069057014032))  # 12,069,057,014_032

print("*" * 80)
# -------------------------
# --- reference opjects----
# -------------------------

a = ["Retention", 3, None, "s"]
b = ["Retention", 3, None, "s"]

print(a is b)
a = 'somthing'
b = None
print(f"{a is not b}\n{b is None}")
a1 = 7

print(0 <= a1 <= 10)
five = 5
two = 2
six = 1
zero = 0
print(five and two)
print(five or six)

p = (4, "frog", 9, -33, 9, 2)
print("dog" not in p)

print(two and zero)
