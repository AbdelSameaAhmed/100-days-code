# for in satatement

for letter in "asdfghjkvye":
    if letter in "ieauo":
        print(f"{letter} is vowel")
    else:
        print(f"{letter} is consonant")


print("#" * 20)
# --------------------------------
# -----try except-----------------
# ----------------------------
# s = input("please enter integer: ")

try:
    i = int(s)
    print(f"{i} is valid integer")
except ValueError as err:
    print(err)

print("*" * 50)
# ----------------------------
# -------Example--------------
# ----------------------------
total = 0
count = 0
while True:
    line = input("integer: ")
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print(err)
            continue
        total += number
        count += 1
    else:
        break
    if count:
        print(f"count = {count}\ntotal = {total}\nmean ={total / count}")
