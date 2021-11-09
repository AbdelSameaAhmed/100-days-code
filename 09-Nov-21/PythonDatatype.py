# -------------------------------------------------
# Variable 
# -------------------------------------------------

# List
print("*"*60)
# A list is a container which holds comma-separated values
#  between square brackets where items or elements need not all have the same type.
# ex
myList = [20, 30, 40, 20, "asa", "com"]
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])
print(myList[4])
print(myList[5])
# print(myList[6]) # IndexError: list index out of range
print("*"*30)
names = ["Sara", "David", "Warner", "Sandy"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
# print(names[4]) # IndexError: list index out of range
print("*"*30)

# append
names += ["asa"]
print(names)
names.append("afa")
print(names)
print("*"*30)
# extend
names1 = names.copy()
names1.extend(myList)
print(names1)
print(names)
print("*"*30)

# Use + operator to create a new list that is a concatenation
# of two lists and use * operator to repeat a list. See the following statements
color_list1 = ['red']
color_list2 = ['gray', 'black']
color_list3 = ['yellow', 'red', 'blue']
color_list = color_list1 + color_list2 + color_list3
print(color_list)
print("*"*30)
# list of integer

numb_int = [1, 20, 30, 4]
print(numb_int[2] * 4)
print(numb_int * 3)
# Add item to list using append
print("*"*30)
color_list.append("orange")
print(color_list)
# Add item to list using +=
color_list +=['white']
print(color_list)
# Add item to list using insert
color_list.insert(0, "blue")
print(color_list)