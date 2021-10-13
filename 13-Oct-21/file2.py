# ------------------
#
# string methodes
#
# -----------------
file = open("textfile.txt", "a+")

file.writelines("this is another line\n")
# ---
# split() 
myString = "I Love Python Very Much"
myString_split = myString.split()
print(myString_split)
type(myString_split)
# rsplit()
myString_rsplit = myString.rsplit(" ",3)
myString_rsplit
type(myString_rsplit) 


# -------------------
# center()
myName = "Asahmed"
print(myName.center(7, "@"))


# ----------------------
# count()
f = "I love python and php so much and php"
print(len(f))
print(f.count("php", 0, 10))
print(f.count("php", 0, len(f)))

# --------------------------
# swapcase()
print(f.swapcase())

# -------------------------------
# startwith()
# startswith(text, start, end)
print(f.startswith("u"))
print(f.startswith("i"))
print(f.startswith("I", 3,19))

# -------------------------------
# endwith()
# endswith(text, start, end)
f = "I love python and php so much and php"
print(f.endswith("u"))
print(f.endswith("p"))
print(f.endswith("p"))
print(f.endswith("I", 3,19))

# ------------------------

# index()
# index(text, start, end)
f = "I love python and php so much and php"
print(f.index("I"))
print(f.index("p", 1, len(f)))


# --------------------------
# rjust(width, fill character)
#ljust(width, fill character)

names = "asahmed"
print(names.rjust(8,"@"))
e='''first
line
is first'''
f1="i love\npython\nvery musch"
print(f1.splitlines())


# ----------------
# Replace()
# ----------------

af = "I have started learn Python have have have"
af.replace("have", "am",2)


# ---------------
# Join()
# ---------------

dd = [ "asa", "ddd", "ala"]

print("/".join(dd))


# ----------------------------------------------------
# concatenate string and number (d, f) with placeholder %s, %d, %f
# %s placeholder for string
# %d placeholder for double
# %f placeholder for float

name = "Asahmed"
age = 47
rank = 10

print("my name is : "+ name + "and my age is: "+ age + "and my rank is: "+ rank)

print("my name is: %s , my age is %d and my rank is: %d" % (name, age, rank))

# -----------------------------------------------
# another modern methode for concatenate string and number
name = "Asahmed"
age = 47
rank = 10
print("my name is {}".format(name))
print("my name is {:s}".format(name))
print("my name is {:s} and my age is {:d} and my rank is {:.2f}".format(name, age, rank))

# -----------------------------------
# mony format
myMony = 12340987457
print("my mony in bank is {:,d}".format(myMony))
print("my mony in bank is {:_d}".format(myMony))
print("my mony in bank is {:,.2f}".format(myMony))

# ----------------------------------
#rearrange items
#using place holder {}
#
a, b, c = 1, 2, 3
print("Hello {0} {1} {2}".format(a, b, c))
print("Hello {2:d} {1:.2f} {0}".format(a, b, c))

# -------------------


# ------------------
# append()
# -----------------
l1 = [1,2,3, "a", "s"]
l1
l1.append(4)
l1.remove(4)
l1

# -----------------------
# extend()

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

a.extend(b)
a.extend(c)


# ------------------------
# sort() and reverse()

a.sort(reverse = True)
print(a)




# ----------------------
# clear()
z=a
print(z)
z.clear()
print(z)


# ----------------------
# copy()

d = [1,2,3,4]
z = [5,6,7,8]

c = z.copy() 
g = z.copy()

# d is main list  
# c is copy of d
# z is main list
# g is a copy of z

# ---------------------------
d.append(4)
d
print(d.count(4))


# ---------------------------------
# insert()
d.insert(0, 'ASA')
d



# ----------------------------------
# pop()

d.pop(1)
d.pop(-1)
print(d)
d.pop(-1)
print(d)


# ---------------------------------------------------
# Practice
#-----------------------------------------------------
# program take name and email from user and return the:
# 1. name
# 2. user name
# 4. email
# 5. domain

theName = input("What\'s your name ").strip().capitalize()
theemail= input("Please enter your email :").strip()
userName = theemail[:theemail.index("@")]
websit = theemail[theemail.index("@"):]

print(f"Hello {theName} your username is {userName} and your websit is {websit}")

