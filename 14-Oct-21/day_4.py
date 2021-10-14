"Day 4 in 100DaysOfcode" 
# dict ------------------
import os
os.chdir(r"C:\Users\asahmed\Documents\GitHub\100DaysOfCode\100-days-code\14-Oct-21")

first_dict = dict()
print(first_dict)
# to add item use []
first_dict["first"] = "one"
print(first_dict)

# example
dict_1 =  {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(dict_1)
len(dict_1)

# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the
# dictionary

print(os.getcwd())
df = open("textfile1.txt")
fil =df.read()
# count = 0
# for line in fil:
#     if count > len(fil):

#         break
#     print(count)
#     count = count + 1

    

fil_dict = {}
index = 0
for lines in fil:
    if index < len(fil):
        if lines not in fil_dict:
            fil_dict[index] = lines
        index += 1
    else:
        break
    

print(fil_dict)

# -----------------------------------------
print("*" * 50)

word = "applications"
dict = {}

for letter in word:
    if letter not in dict:
        dict[letter] = 1
    else:
        dict[letter] = dict[letter] +1 
print(dict)
print(dict.get("a"))
# -----------------------------------------

print("*" * 50)

word = 'brontosaurus'
d = {}
for c in word:
    d[c] = d.get(c,0) + 1
print(d)
    
# -----------------------------------------
print("*" * 50)

print("*" * 50)
## dictionary with File
# recive file name from user
fname = input("please enter file name: ")

# use try except to read FileExistsError


try:
    fhand = open(fname)
except:
    print("file can not be opend")
    exit()
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[words] += 1
print(counts)



