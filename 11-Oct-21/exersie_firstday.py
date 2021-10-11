# Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards
word = input("PLZ enter word: ")
count = 0
letter = len(word)-1
while count < len(word):
    count += 1
    letter = word[count-1]
    print(letter)